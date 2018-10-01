#!/usr/bin/python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]  # n is row of pancake, m is size of spatula
  m = int(m)
  stringList = list(n)
  flips = 0
  check = True
  for k in range(0, len(stringList)):
	if(stringList[k] == "-"):
		flips += 1
		for l in range(k, k+m):
			if(l < len(stringList)):
				if(stringList[l] == "+"):
					stringList[l] = "-"
				elif(stringList[l] == "-"):
					stringList[l] = "+"
			else:
				check = False
				break

  if(check == False):
	print "Case #{}: {}".format(i, "IMPOSSIBLE")
  else:
    print "Case #{}: {}".format(i, flips)
  # check out .format's specification for more formatting options