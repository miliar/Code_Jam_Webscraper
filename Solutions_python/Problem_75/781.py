f = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(f.readline())

for i in xrange(0, n):
  seq = f.readline().split()
  cnt = 0
  m = int(seq[cnt])
  #print(m)
  cnt += 1
  cmb = {}
  for j in xrange(0, m):
    st = seq[cnt]
    cnt += 1
    cmb[st[0] + st[1]] = st[2]
    cmb[st[1] + st[0]] = st[2]
    
  #print(cmb)  
    
  m = int(seq[cnt])
  cnt += 1
  clr = {}
  for j in xrange(0, m):
    st = seq[cnt]
    cnt += 1
    clr[st[0] + st[1]] = True
    clr[st[1] + st[0]] = True
    
  #print(clr)
    
  m = int(seq[cnt])
  cnt += 1
  l = []
  for j in xrange(0, m):
    val = seq[cnt][j]
    #print(val)
    while len(l) != 0 and (l[len(l) - 1] + val) in cmb:
      val = cmb[l[len(l) - 1] + val]      
      l.pop()
      
    #print(l)  
    cleared = False  
    for k in l:
      if (k + val) in clr:
        l = []
        cleared = True
        break;
      
    if not cleared: l.append(val)
    
  fout.write('Case #')
  fout.write(str(i + 1))
  fout.write(': ')
  fout.write('[')
  mmm = 0
  for v in l:
    fout.write(v)
    mmm += 1
    if mmm != len(l):
      fout.write(', ')
  fout.write(']')
  fout.write("\n")
  
fout.close()
f.close()