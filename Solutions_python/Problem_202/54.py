from collections import defaultdict
from ortools.linear_solver import pywraplp
from collections import defaultdict
import sys
import time
from multiprocessing.pool import Pool

class ThreadRes(object):
    def __init__(self):
        self.res = None

def board_ilp_thread(n, m, v_ri_ci, tr,
                     optimization_problem_type=pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING):
    res = board_ilp(n, m, v_ri_ci,
              optimization_problem_type=pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    tr.res = res

def board_ilp(n, m, v_ri_ci,
              optimization_problem_type=pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING):
    sys.setrecursionlimit(100000)
    solver = pywraplp.Solver('board_ilp', optimization_problem_type)
    infinity = solver.infinity()
    o = [solver.IntVar(0.0, 1, 'o,' + str(i/n) + "," + str(i%n)) for i in xrange(n*n)]
    x = [solver.IntVar(0.0, 1, 'x,' + str(i/n) + "," + str(i%n)) for i in xrange(n*n)]
    p = [solver.IntVar(0.0, 1, '+,' + str(i/n) + "," + str(i%n)) for i in xrange(n*n)]
    rows_dict = defaultdict(int)
    cols_dict = defaultdict(int)
    diag0_dict = defaultdict(int)
    diag1_dict = defaultdict(int)
    solver.Maximize(solver.Sum(map(lambda oi: 2*oi, o)+x+p))

    for r in xrange(n):
        for c in xrange(n):
          d0 = r+c
          d1 = r-c
          rows_dict[r] += o[r*n+c] + x[r*n+c]
          cols_dict[c] += o[r*n+c] + x[r*n+c]
          diag0_dict[d0] += o[r*n+c] + p[r*n+c]
          diag1_dict[d1] += o[r*n+c] + p[r*n+c]
          solver.Add(o[r*n+c] + x[r*n+c] + p[r*n+c] <= 1)

    for k, v in rows_dict.iteritems():
        solver.Add(v <= 1)

    for k, v in cols_dict.iteritems():
        solver.Add(v <= 1)

    for k, v in diag0_dict.iteritems():
        solver.Add(v <= 1)

    for k, v in diag1_dict.iteritems():
        solver.Add(v <= 1)

    for v, ri, ci in v_ri_ci:
        if v == '+':
            solver.Add(o[ri*n+ci] + p[ri*n+ci] == 1)
        elif v == 'x':
            solver.Add(o[ri*n+ci] + x[ri*n+ci] == 1)
        else:
            solver.Add(o[ri*n+ci] == 1)

##    SolveAndPrint(solver, o+x+p)
    return solve(solver, o+x+p)

def solve(solver, variable_list):
    v_ri_ci = set()
    result_status = solver.Solve()
##    assert result_status == pywraplp.Solver.OPTIMAL
##    assert solver.VerifySolution(1e-7, True)
    for variable in variable_list:
        if variable.solution_value():
            v, ri, ci = variable.name().split(",")
            v_ri_ci.add((v, int(ri), int(ci)))
    return int(round(solver.Objective().Value(), 0)), v_ri_ci

def SolveAndPrint(solver, variable_list):
  """Solve the problem and print the solution."""
  print(('Number of variables = %d' % solver.NumVariables()))
  print(('Number of constraints = %d' % solver.NumConstraints()))

  result_status = solver.Solve()

  # The problem has an optimal solution.
  assert result_status == pywraplp.Solver.OPTIMAL

  # The solution looks legit (when using solvers others than
  # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
  assert solver.VerifySolution(1e-7, True)

  print(('Problem solved in %f milliseconds' % solver.wall_time()))

  # The objective value of the solution.
  print(('Optimal objective value = %f' % solver.Objective().Value()))

  # The value of each variable in the solution.
##  for variable in variable_list:
##    if variable.solution_value():
##        print(('%s = %f' % (variable.name(), variable.solution_value())))

  print('Advanced usage:')
  print(('Problem solved in %d branch-and-bound nodes' % solver.nodes()))


def main(fname):
    before = time.time()
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    p_res = [0]*4
    p_v_ri_ci = [0]*4
    pool = Pool(processes=4)
    for i in xrange(t/4):
        for k in xrange(4):
            print "Case " + str(i*4+k)
            n, m = map(int, in_fd.readline().strip().split(" "))
            v_ri_ci = set()
            for j in xrange(m):
                v, ri, ci = in_fd.readline().strip().split(" ")
                v_ri_ci.add((v, int(ri)-1, int(ci)-1))
            start = time.time()
    ##        profit, new_v_ri_ci = board_ilp(n, m, v_ri_ci)
            p_res[k] = pool.apply_async(board_ilp, (n, m, v_ri_ci))
            p_v_ri_ci[k] = v_ri_ci
        for k in xrange(4):
            profit, new_v_ri_ci = p_res[k].get()
            print(time.time() - start)
            new_v_ri_ci -= p_v_ri_ci[k]
            out_fd.write("Case #%d: %d %d\n" % (i*4+k+1, profit, len(new_v_ri_ci)))
            for v, ri, ci in new_v_ri_ci:
                out_fd.write(" ".join([v, str(ri+1), str(ci+1)])+"\n")
    in_fd.close()
    out_fd.close()
    print(time.time() - before)
