br = open('A-large.in')
pw = open('a-large.out', 'w')

f = lambda: br.readline().split()
t = int(f()[0])

for i in range(1, t + 1):
  p = f()
  s = [int(c) for c in p[1]]
  cnt, r = 0, 0
  for j in range(len(s)):
    cnt += s[j]
    if cnt < j + 1:
      r += (j + 1) - cnt
      cnt += (j + 1) - cnt
  pw.write("Case #%d: %d\n" % (i, r))
  print r
