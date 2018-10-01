# -*- coding: utf-8 -*-
fname = "C-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

def xorsum(nums):
    a = 0
    for n in nums:
        a ^= n
    return a

numcases = gcj_read()[0]

for caseno in range(numcases):
    _ = fin.readline()
    candyvals = gcj_read()
    if xorsum(candyvals) == 0:
        outstr = str(sum(candyvals) - min(candyvals))
    else:
        outstr = "NO"
    print candyvals, outstr
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
