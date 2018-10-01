#!/usr/bin/python

import os,sys,string

class impossibru(Exception):
  def __init__(self, value):
    self.value=value
  def __str__(self):
    return repr(self.value)

upperbound=100

def check_line(line,n):
  for i in range(len(line)):
    if not(line[i]==""):
      if int(line[i])>n:
        return 0
  return 1

def find_first_coords_of(n,pattern,dims):
  match=str(n)
  for r in range(dims[0]):
    for c in range(dims[1]):
      if pattern[r][c]==match:
        return [r,c]
  return [-1,-1]

def undo_mow(pattern,coord,direction):
  if direction=="row":
    pattern[coord]=["" for char in pattern[coord]]
  elif direction=="col":
    for r in range(len(pattern)):
      pattern[r][coord]=""
  return pattern

fname=sys.argv[1]
fhandle=open(fname,"r")

ncases=int(fhandle.readline())

for case in range(ncases):
  prefix="Case #"+str(case+1)+": "

  dims=[int(dim) for dim in fhandle.readline().split(" ")]

  pattern=[]
  for row in range(dims[0]):
    pattern.extend([fhandle.readline().rstrip().split(" ")])

  possible=True
  try:
    for n in range(1,upperbound+1):
      find_n=True
      while find_n:
        [r,c]=find_first_coords_of(n,pattern,dims)
        if r==-1:
          find_n=False
        else:
          check_row=check_line(pattern[r],n)
          check_col=check_line([ pattern[i][c] for i in range(dims[0]) ],n) 
          if not(check_row or check_col):
            raise impossibru("yolo")
          else:
            if check_row:
              pattern=undo_mow(pattern,r,"row")
            if check_col:
              pattern=undo_mow(pattern,c,"col")
    final="".join([ "".join(pattern[i]) for i in range(dims[0]) ])
    if final=="":
      print prefix+"YES"
    else:
      print prefix+"UNKNOWN ERROR"
  except impossibru:
    print prefix+"NO"
