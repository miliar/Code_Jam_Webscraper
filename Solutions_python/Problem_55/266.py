# -*- coding: utf-8 -*-
fname = "C-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  linebits = [int(numb) for numb in linestr.split()]
  #if len(linebits) == 1:
    #return linebits[0]
  #else:
  return linebits

numcases = gcj_read()[0]

for caseno in range(numcases):
  R, k, N = gcj_read()
  groups = gcj_read()
  possloads = []
  for i, group in enumerate(groups):
    load = group
    next = (i+1) % N
    while next != i:
      if load + groups[next] > k:
	break
      load += groups[next]
      next += 1
      next %= N
    possloads.append((load, next))
  
  #print possloads
  loadorder = []
  nextstarts = []
  start = 0
  while True:
    if start in nextstarts:
      loopto = nextstarts.index(start)
      loop = loadorder[loopto:]
      startup = loadorder[:loopto]
      break
    nextstarts.append(start)
    load, start = possloads[start]
    loadorder.append(load)
    
    
    
  print startup, loop, R
  if R <= len(startup):
    goes = sum(startup[:R])
  else:
    goes = sum(startup)
    R -= len(startup)
    goes += (sum(loop) * int(R/len(loop)))
    R %= len(loop)
    goes += sum(loop[:R])
  fout.write("Case #"+str(caseno+1)+": "+ str(goes) +"\n")

fin.close()
fout.close()