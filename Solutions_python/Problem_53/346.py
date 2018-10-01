#! /usr/bin/python

fd = open("input.in")

def solve(n, k):
  final = k % (1 << n)

  for i in xrange(0, n):
    if (final & (1 << i)) == 0:
      return "OFF"

  return "ON"

num_cases = int(fd.readline())

for i in range(0, num_cases):
  (n, k) = [int(item) for item in fd.readline().split(" ")]
  output = solve(n, k)
  print "Case #%d:" % (i+1), output

