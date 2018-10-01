import sys
import itertools

fin = sys.stdin
fout = open('split.out','w')
T = int(fin.readline())
for case in range(1,T+1):
  num = int(fin.readline())
  temp = str(fin.readline()).split()
  vals = []
  for i in temp:
    vals.append(int(i))
  possible = False
  maxsum = 0
  for i in range(1,num):
    pat = itertools.combinations(vals,i)
    sean = itertools.combinations(vals,num-i)
    patsums = []
    seansums = []
    truepat = []
    for j in pat:
      patsum = 0
      for k in j:
        patsum = patsum ^ k
      patsums.append(patsum)
      truepat.append(sum(j))
    for j in sean:
      seansum = 0
      for k in j:
        seansum = seansum ^ k
      seansums.append(seansum)
    for j in range(0,len(patsums)):
      if patsums[j] == seansums[-j-1]:
        if truepat[j] > maxsum:
          possible = True
          maxsum = truepat[j]
  if not possible: 
    fout.write("Case #{0}: NO\n".format(case))
  else:
    fout.write("Case #{0}: {1}\n".format(case,maxsum))
  
fout.close()


