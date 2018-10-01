#/bin/python.exe
import sys
""" approach: if all the numbers xor to 0, there is a solution
      (that solution is the smallest number, which he gives away).  
   Otherwise, no solution.
"""

def solve_case(line_input):
  array = [int(x) for x in line_input.split(" ")]
  if reduce(lambda x, y: x^y, array) == 0:
    return str(sum(array) - min(array))
  else:
    return "NO"

#main
input_f = open(sys.argv[1])
num_cases = int(input_f.readline())
for c in xrange(1, num_cases+1):
  input_f.readline() #ignore every other line of input
  print "Case #%d: %s" % (c, solve_case(input_f.readline().strip()))

