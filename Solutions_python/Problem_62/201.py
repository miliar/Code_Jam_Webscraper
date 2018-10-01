import sys
from math import sqrt

Q = int(sys.stdin.readline().strip())

def intall(x): return int(x)
def add(x,y): return x+y
def cross(X,Y):
  [x,y] = X
  [z,q] = Y
  if x > z and y < q:
    return True
  if x < z and y > q:
    return True
  return False

for qw in range(1, Q+1):
  print 'Case #%d:' % qw,
  ###
  W = int(sys.stdin.readline().strip())
  wires = []
  for qe in range(1, W+1):
    nums = sys.stdin.readline().strip()  
    wire = nums.split()
    wire = map(intall,wire)
    wires.append(wire)
  cnt = 0
  for qe in range(0,W-1):
    X = wires[qe]
    for qr in range(qe+1,W):
      Y = wires[qr]
      if cross(X,Y):
        cnt += 1
  print cnt
#  nums = num.split()
#  nums = map(intall, nums)
#  for n in nums:
#  
#  print nums
  ###
  ###
#  result = 0 ##change this
#!!!!
#  print result