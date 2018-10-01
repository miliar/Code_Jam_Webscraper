import sys
import heapq as hq

def sol(N, K):
  gap=[]
  hq.heappush(gap,-N)
  for i in range(K-1):
    m = -hq.heappop(gap)
    m1=int(m/2)
    m2=m-int(m/2)-1
    hq.heappush(gap,-m1)
    hq.heappush(gap,-m2)
  m=-hq.heappop(gap)
  return int(m/2), m-int(m/2)-1
  
f=open('solut.txt','w')
with open(sys.argv[1]) as fh:
    N = int(next(fh))
    i = 1
    for line in fh:
      a,b = line.split()
      a=int(a)
      b=int(b)
      s=sol(a,b)
      print("Case #{}: {} {}".format(i, s[0], s[1]),file=f)
      i += 1
        
f.close
