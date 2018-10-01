


def solution(S, k):
  n = len(S)
  m = 0
  c = 0
  for i in range(n-k+1):
    if S[i] == "-":
      c+=1
      m+=1
      for j in range(k):
        if S[i+j] == "-":
          S[i+j] = "+"
        else:
          S[i+j] = "-"
  impossible = False

  for j in xrange(n-k+1, n):
    if S[j] == "-":
      impossible = True
      break
  
  if impossible:
    return "IMPOSSIBLE"
    
  else:
    return str(c)


tc = int(raw_input())
for t in range(1, tc+1):
  s = raw_input().split()
  S = list(s[0])
  k = int(s[1])
  print "Case #"+str(t)+": "+solution(S, k)
