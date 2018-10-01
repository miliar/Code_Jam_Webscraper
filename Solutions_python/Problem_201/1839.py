from __future__ import print_function
import fileinput
import math
import Queue as Q

class R(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.size = end-start+1
    self.stall = start + int(math.floor((end-start)/2))
    #print(start, end)

  def __cmp__(self, other):
    return cmp(other.size, self.size)

f = fileinput.input()

T = int(f.readline())
for case in range(1, T + 1):
  N,K = f.readline().rstrip().split()
  N = int(N)
  K = int(K)

  q = Q.PriorityQueue()
  q.put(R(0, N-1))

  s = 0
  r = None
  for user in range(0, K):
    r = q.get()
    s = r.stall
    q.put(R(r.start, s-1))
    q.put(R(s+1, r.end))

  a = s - r.start
  b = r.end -s
  print("Case #"+str(case)+": "+str(max(a,b))+" "+str(min(a,b)))
