
import os
import fileinput
import math
import pdb
import re
import getopt,sys
import copy



def readMat(filename) :
#  pdb.set_trace()
  result = []
  mfile = fileinput.input(filename)
  for line in mfile :
    ar = line.split()
    if len(ar)>0 :
      row = []
      for item in ar :
        value = float(item)
        row.append(value)
      result.append(row)
  return result



if len(sys.argv)<2:
  print('input file needed')
  sys.exit()

fname=sys.argv[1]
print(fname)

mat=readMat(fname)

assert len(mat)>0

ncases = int(mat[0][0])

print(ncases)

outfname='out.txt'
of = open(outfname, 'w')

assert len(mat)>=(ncases*2+1)
for i in range(0, ncases):
    print('Case #'+str(i+1))

    assert len(mat[i*2+1])>2
    r = int(mat[i*2+1][0])
    k = int(mat[i*2+1][1])
    n = int(mat[i*2+1][2])
    print([r,k,n])
    gps=[]
    assert len(mat[i*2+2])==n
    for v in mat[i*2+2]:
      gps.append(int(v))

    print('gps')
    print(gps)
    nppls=n*[int(0)]
    gstops=n*[int(0)]

    sum=0
    for j in range(0,n):
        sum += gps[j]
    if k>=sum:
        for j in range(0,n):
            nppls[j]=sum
            gstops[j]=j
    else:
        for j in range(0,n):
            nppls[j]=0
            l=j
            while(nppls[j]+gps[l]<=k):
                nppls[j]+=gps[l]
                l=(l+1)%n
            gstops[j]=l
    #now find the loop
    print('sum')
    print(sum)
    print('gstops')
    print(gstops)
    print('nppls')
    print(nppls)
    cur=0
    track=[]
    trackppls=0
    while(not cur in track):
        assert gstops[cur]>=0 and gstops[cur]<n
        track.append(cur)
        trackppls+=nppls[cur]
        cur=gstops[cur]
    iterhead=cur
    print('iterhead')
    print(iterhead)
    print('track')
    print(track)

    pplsbegin=0
    headlen=0
    if not iterhead==0:
        cur =0
        while(not cur==iterhead):
            pplsbegin+=nppls[cur]
            headlen+=1
            cur=gstops[cur]

    iterppls=trackppls-pplsbegin
    print('pplsbegin')
    print(pplsbegin)
    print('trackppls')
    print(trackppls)
    print('iterppls')
    print(iterppls)
    print('headlen')
    print(headlen)

    #now calculate for result
    if r<len(track):
        totalppls = 0
        for j in range(0, r):
            totalppls += nppls[track[j]]
    else:
        riter,rres=divmod((r-headlen),(len(track)-headlen))
        totalppls=pplsbegin
        totalppls+= riter*iterppls
        for j in range(headlen, headlen+rres):
            totalppls+=nppls[track[j]]
            

    line='Case #'+str(i+1)+': '+str(totalppls)+'\n'
    of.write(line)


    
    




of.close()
