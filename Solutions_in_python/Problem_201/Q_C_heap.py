from heapq import heappush, heappop
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):  
  n,m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this cas
  # holder=Node(n)
  heap = []
  heappush(heap, -n)
  while(m>0):
    n=heappop(heap)
    # print n
    m=m-1
    Z=-(abs(n)/2)
    heappush(heap, Z)
    W=-((abs(n)-1)/2)
    heappush(heap, W)
  # print [heappop(heap) for i in range(len(heap))]
  a=abs(n)/2
  b=(abs(n)-1)/2

  print "Case #{}: {} {}".format(i, a,b )
  