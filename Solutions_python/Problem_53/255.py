# -*- coding: utf-8 -*-
fname = "A-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  linebits = [int(numb) for numb in linestr.split()]
  if len(linebits) == 1:
    return linebits[0]
  else:
    return linebits

numcases = gcj_read()

for caseno in range(numcases):
  N, K = gcj_read()
  toloop = 2**N
  if K % toloop == toloop - 1:
    fout.write("Case #"+str(caseno+1)+": ON\n")
  else:
    fout.write("Case #"+str(caseno+1)+": OFF\n")

fin.close()
fout.close()