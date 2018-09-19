from itertools import product

def pal (a):
  return str(a) == str(a)[::-1]

digits = "012"

res1 = [0] * 1000000

for i in range (4):
  res1[i] = i
n = 4

for k in range (23):
  for p in product ("01", repeat = k):
    t = "1" + "".join(p);
    s = int (t + t[::-1])
    if pal (s * s):
      res1[n] = s
      n += 1
    for d in digits:
      s = int (t + d + t[::-1])
      if pal (s * s):
        res1[n] = s
        n += 1
  t = '2' + ('0' * k)
  s = int (t + t[::-1])
  res1[n] = s
  n += 1
  for d in "01":
    s = int (t + d + t[::-1])
    res1[n] = s
    n += 1

print n
res1 = list(set(res1))

res1.sort()
for i in range (len (res1)):
  print res1[i]
