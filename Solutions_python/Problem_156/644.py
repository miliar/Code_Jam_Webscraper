import sys
from math import ceil

def try_stacksize(diners, stacksize):
  mins = stacksize
  for diner in diners:
    mins = mins + ceil(diner/stacksize) - 1
  return mins

def solve(diners):
  diners = list(diners)
  if diners == [1]:
    return 1
  top = max(diners)
  best = 999999999999999999
  for i in range(2, top+1):
    res = try_stacksize(diners, i)
    if res < best:
      best = res
  return best

def solve_case(case_num, line):
  diners = map(int, line.split(' '))
  solution = solve(diners)
  print("Case #{}: {}".format(case_num, solution))

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
        from http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

if __name__ == "__main__":
  for case_num, case in list(enumerate(sys.stdin.read().splitlines()[0:][::2]))[1:]:
    solve_case(case_num, case)
