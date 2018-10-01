import sys

Q = int(sys.stdin.readline().strip())

def intall(x): return int(x)
def add(x,y): return x+y
def delj(x,y): return x*1.0/y

def pred(s,ts,i):
  k = s[i]
  cnt = 0
  if (ts[i]=='X'):
    return len(s)+1
  for j in range(0,len(s)):
    if s[j]>k and ts[j]=='X':
      cnt += 1
  return cnt  

for qw in range(1, Q+1):
  print 'Case #%d:' % qw,
  ###
  nums1 = sys.stdin.readline().strip()
  nums2 = sys.stdin.readline().strip()
  nums3 = sys.stdin.readline().strip()
  
  nums1 = nums1.split()
  [N,K,B,T] = map(intall, nums1)
  
  nums2 = nums2.split()
  pot = map(intall, nums2)

  nums3 = nums3.split()
  vel = map(intall, nums3)
  
  ds = [B-s for s in pot]
  ts = map(delj,ds,vel)
  
  for i in range(0,len(ts)):
    if ts[i] > T:
      ts[i] = 'X'
  count = ts.count('X')

  if not count > N-K:
    for i in range(0,len(ts)):
      if ts[i] > T:
        ts[i] = 'X'
  
    all = []
    for i in range(0,len(pot)):
      all.append(pred(pot,ts,i))
    all.sort()
    cnt = 0;
   # print all
    for k in range(0,K):
      cnt += int(all[k]) 
    print cnt
  else: 
    print 'IMPOSSIBLE'