import sys


def solve_test(inp):
    ac, aj = map(int, inp.readline().split())
    J = []
    C = []
    for _ in range(ac):
      st, end = map(int, inp.readline().split())
      C.append((st,end, 'c'))
    for _ in range(aj):
      st, end = map(int, inp.readline().split())
      J.append((st,end, 'j'))
    C.sort()
    J.sort()
    C_total = sum(x[1] - x[0] for x in C)
    J_total = sum(x[1] - x[0] for x in J)
    if C_total > J_total:
      T = C
      k = 'c'
      free = 12 * 60 - C_total
    else:
      T = J
      k = 'j'
      free = 12 * 60 - J_total
    #print(T)
    if len(T) == 1:
      return '2'
    all_act = C + J
    all_act.sort()
      
    gaps = [y[0] - x[1] for x, y in zip(all_act, all_act[1:]) if x[2] == y[2] and x[2] == k]
    if  all_act[0][2] == k and all_act[-1][2]==k:
      gaps += [all_act[0][0] - all_act[-1][1] + 24 * 60]
    gaps.sort()
    closed = 0
    #print(gaps, free)
    for g in gaps:
      if free >= g:
        closed += 1
        free -= g
      else:
        break
    total = len(T) - closed
    return str(2 * total) 

inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()