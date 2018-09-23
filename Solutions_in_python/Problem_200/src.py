t = int(input())
for i in range(1, (t + 1)):
  n = int(input())
  s = [int(x) for x in str(n)]
  while (sorted(s) != s):
      n -= 1
      s = [int(x) for x in str(n)]
  print("Case #"+str(i)+": "+str(n))
 
