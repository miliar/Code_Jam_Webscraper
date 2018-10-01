f=open("B-large.in","r")
g=open("cookie.out","w")

def trunc(f, n):
    slen = len('%.*f' % (n, f))
    return str(f)[:slen]

T = int(f.readline())

for i in range(0,T):
  [C,F,X] = map(float,f.readline().split())
  
  v = X/C - 2/F
  if v-round(v) < 0:
    k = int(round(v)-1)
  else:
    k = int(round(v))


  if k > 0:
    s = 0.
    for j in range(0,k):
      s = s + C/(2+j*F)
    ans = s+ X/(2+k*F)
  else:
    ans = X/2

  g.write("Case #"+str(i+1)+": "+str(trunc(ans,7))+"\n")

  
  
  
