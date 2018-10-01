T = int(raw_input())
best = 0

def surprise(x0,x1,x2):
  if(x2 - x0 == 2): return 1
  return 0

for i in range(T):
  line = raw_input().strip().split()
  N = int(line[0])
  S = int(line[1])
  P = int(line[2])
  line = line[3:]
  best = 0
  for a0 in range(11):
    for a1 in range(a0,11):
      for a2 in range(a1,11):
        if(a2 - a0 > 2 or a0 + a1 + a2 != int(line[0])): continue
        if(N == 1):
          if(S == surprise(a0,a1,a2)):
            ans = 0
            if(a2 >= P): ans += 1
            best = max(best,ans)
        else:
          for b0 in range(11):
            for b1 in range(b0,11):
              for b2 in range(b1,11):
                if(b2 - b0 > 2 or b0 + b1 + b2 != int(line[1])): continue
                if(N == 2):
                  if(S == surprise(a0,a1,a2) + surprise(b0,b1,b2)):
                    ans = 0
                    if(a2 >= P): ans += 1
                    if(b2 >= P): ans += 1
                    best = max(best,ans)
                else:
                  for c0 in range(11):
                    for c1 in range(c0,11):
                      for c2 in range(c1,11):
                        if(c2 - c0 > 2 or c0 + c1 + c2 != int(line[2])): continue
                        if(S == surprise(a0,a1,a2) + surprise(b0,b1,b2) + surprise(c0,c1,c2)):
                          ans = 0
                          if(a2 >= P): ans += 1
                          if(b2 >= P): ans += 1
                          if(c2 >= P): ans += 1
                          best = max(best,ans)
  print "Case #%d: %d"%(i+1,best)
