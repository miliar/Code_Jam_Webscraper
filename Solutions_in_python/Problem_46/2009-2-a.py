from gcjt import *
def nn(s,n):
      for i in range(n):
            if s[n-1-i]=='1':return i
      return n
for t in tests():
      n = int(t.rl())
      k = [nn(t.rl(),n) for i in range(n)]
      u = 0
      for i in range(n):
            for j in range(n-i):
                  if k[j]>=n-1-i:
                        del k[j]
                        u+=j
                        break
      t.answer(u)
