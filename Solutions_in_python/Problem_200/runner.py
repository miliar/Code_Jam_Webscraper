from pancakes import solve
from tidy import last_tidy

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  # n, m = [(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  number = int(raw_input())
  result = last_tidy(number)
  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options
