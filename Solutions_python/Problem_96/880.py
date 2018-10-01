#
import re
import math

f = open("B-large.in","r")
fo = open("B-large.out","w")

lines = f.readlines()
lines = [l.strip() for l in lines]
nlines = len(lines)
i = 0

T = int(lines[i])
for icase in range(T):
      # set parameters
      i = i + 1
      l = re.split(" ",lines[i])
      n = int(l[0])
      s = int(l[1])
      p = int(l[2])
      t = [int(x) for x in l[3:]]
      min_sup = max(p * 3 - 4, p)
      max_sup = p * 3 - 3
      good = 0
      border = 0
      for j in range(n):
            if t[j] >= min_sup:
                  if t[j] > max_sup:
                        good = good + 1
                  else:
                        border = border + 1
      ans = good + min(border, s)
     
      print("Case #",icase+1,": ",ans,sep="",file=fo)
      print("Case #",icase+1,": ",ans,sep="")

#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()




