#!/usr/bin/python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = raw_input()  # n is number
  num = int(n)
  lastNice = 0
  for j in xrange(num, 0, -1):
    tempStr = str(j)
    intList = list(tempStr)
    numCheck = True
    
    if(all(intList[k] <= intList[k+1] for k in xrange(len(intList)-1))):
        lastNice = j
        break
  
  print "Case #{}: {}".format(i, lastNice)