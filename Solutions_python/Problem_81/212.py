import sys
def read_values():
  return map(int,raw_input().split())

for case_index in range(1, 1+input()):

  n = input()
  l = []
  for i in range(n):
    l.append(raw_input().strip())
  wp = [(0,0.0) for i in range(n)]
  for i in range(n):
    for j in range(n):
      if l[i][j] == '1':
        w,m = wp[i]
        wp[i] = (w+1,m+1)
      elif l[i][j] == '0':
        w,m = wp[i]
        wp[i] = (w,m+1)

  owp = [(0.0,0.0) for i in range(n)]
  for i in range(n):
    for j in range(n):
      if l[i][j]!='.':
        a,b = owp[i]
        num,den = wp[j]
        if l[j][i]=='1':
          num -= 1
        den -= 1

        a += num/float(den)
        b += 1
        owp[i] = (a,b)

  oowp = [(0.0,0.0) for i in range(n)]
  for i in range(n):
    for j in range(n):
      if l[i][j]!='.':
        num,den = owp[j]
        a,b = oowp[i]
        a += num/float(den)
        b += 1
        oowp[i] = (a,b)
  v = []
  for i in range(n):
    v.append(.25*wp[i][0]/wp[i][1]+0.5*owp[i][0]/owp[i][1]+\
      0.25*oowp[i][0]/oowp[i][1])
  res = "\n".join(map(str,v))
  sys.stderr.write(str(case_index)+' ')
  print 'Case #%s:\n%s'%(case_index,res)

sys.stderr.write('\n')
