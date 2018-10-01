#!/usr/bin/python

# filename = "sample.in"
# filename = "A-small-attempt0.in"
filename = "A-large.in"

inp = open(filename, "rU")

n = int(inp.readline().strip())

for case in range(1, n+1):
  count = 0
  friends = 0
  for i, o in enumerate(inp.readline().strip().split(" ")[1]):
    o = int(o)
    if o > 0 and i > count:
      f = (i - count)
      friends += f
      count += f
    count += o

  answer = friends
  print("Case #{}: {}".format(case, answer))
