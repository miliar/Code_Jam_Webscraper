
def solve(casenr):
  n = int(raw_input())
  #a = (\x -> double(x)) raw_input().split(str=" ")
  a = map(lambda x: float(x), raw_input().split(" "))
  b = map(lambda x: float(x), raw_input().split(" "))
  a.sort(reverse=True);
  b.sort(reverse=True);
  pts = 0
  aa = a[:]
  bb = b[:]
  #print aa
  #print bb
  for i in range(0, n): 
    if b[0] > a[0]:
      del b[0]
      del a[0]
    else:
      del a[0]
      del b[-1]
      pts += 1
  p2 = 0
  for cnt in range(0, n):
    win = True
    for idx in range(0, n - cnt):
      aidx = n - 1 - cnt - idx
      bidx = n - 1 - idx
      #print aidx, bidx
      if aa[aidx] < bb[bidx]:
        win = False
        break
    if win:
      p2 = n - cnt
      break
  print "Case #" + str(casenr) + ":", p2, pts  

case = int(raw_input())
for n in range( 0, case):
  solve(n+1)

