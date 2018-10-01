f = open('A-large.in')
o = open('output.txt', 'w')
n = int(f.readline())

for i in range(n):
  s_max, counts = f.readline().strip().split(" ")
  curr = 0
  res = 0
  for j in range(int(s_max)+1):
    if curr < j:
      curr += 1
      res += 1
    curr += int(counts[j])
  o.write("Case #"+str(i+1)+": "+str(res)+"\n")

f.close()
o.close()