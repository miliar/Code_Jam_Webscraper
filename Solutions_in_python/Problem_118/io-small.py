#!/usr/bin/python
import sys,os

def get_n_palin_sqrs(a,b,palin_squares):
  new_list=palin_squares[:]
  while len(new_list)>0:
    if new_list[0]<a:
      del new_list[0]
    else:
      break
  while len(new_list)>0:
    if new_list[-1]>b:
      del new_list[-1]
    else:
      break
  return len(new_list)

palinhandle=open("fair_n_square_small_list","r")
palin_squares=[int(x.rstrip()) for x in palinhandle.readlines()]
palinhandle.close()

fname=sys.argv[1]
fhandle=open(sys.argv[1],"r")

ncases=int(fhandle.readline().rstrip())
for i in range(ncases):
  prefix="Case #"+str(i+1)+": "
  [a,b]=[int(x) for x in fhandle.readline().rstrip().split()]
  npalin=get_n_palin_sqrs(a,b,palin_squares)
  print prefix+str(npalin)
fhandle.close()
