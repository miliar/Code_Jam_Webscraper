def isTidy(n):
 p = [int(x) for x in list(str(n))]
 return all(p[i]<=p[i+1] for i in xrange(len(p)-1))

def maxSubTidy(n):
 while not isTidy(n):
  p = [int(x) for x in list(str(n))]
  i = 0
  while i < len(p)-1:
   if p[i] > p[i+1]:
    for j in xrange(i+1,len(p)):
     p[j] = 0
    break
   i += 1
  m = "".join(str(x) for x in p)
  n = int(m) - 1
 return n

fname = "B-large"


with open(fname + ".in","r") as f:
 inp = [l.strip('\n') for l in f.readlines()]

f = open(fname + ".out","w")
for i in range(int(inp[0])):
 j = i+1
 data = inp[j]
 result = maxSubTidy(int(data))
 f.write("Case #" + str(j) + ": " + str(result) + "\n")

f.close()
