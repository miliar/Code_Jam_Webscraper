from horses import solve

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  distance, nhorses = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  horses = [[int(s) for s in raw_input().split(" ")] for j in range(nhorses)]
  # number = int(raw_input())
  result = solve(distance, horses)
  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options
