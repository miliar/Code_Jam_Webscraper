#!/usr/bin/python

import sys


def read_data(input):
   O = []
   B = []
   items = input.split()
   elems = int(items[0])
   for x in range(elems):
      if items[1 + x * 2] == "O":
         O.append((x, int(items[2 + x * 2])) )
      else:
         B.append((x,int(items[2 + x * 2]) ))
   O.reverse()
   B.reverse()
   return (O,B)

def solve(data):
   (O,B) = data
   time = 0
   i = 0
   oPos = 1
   bPos = 1
   while O or B:
     button = 0
     time = time + 1
     if O:
        if O[-1][0] == i and O[-1][1] == oPos:
           # is active
	   O.pop()
           button = 1
        else:
           if oPos != O[-1][1]:
              if oPos < O[-1][1]:
                 oPos += 1
              if oPos > O[-1][1]:
                 oPos -= 1
     if B:
        if B[-1][0] == i and B[-1][1] == bPos:
           # is active
	   B.pop()
           button = 1
        else:
           if bPos != B[-1][1]:
              if bPos < B[-1][1]:
                 bPos += 1
              if bPos > B[-1][1]:
                 bPos -= 1
     if button:
        i = i + 1
     #print "Time: %d, i: %d, oPos: %d, bPos: %d" % (time, i, oPos, bPos)
   return time
def do_prob(i, data):
   data = read_data(data)
   sol = solve(data) 
   print "Case #%d: %d" % (i, sol)

if __name__ == "__main__":
   input = open(sys.argv[1])
   num_inputs = int(input.readline())
   for i in range(num_inputs):
	do_prob(i+ 1, input.readline())

