#! /usr/bin/python
import sys
import os

filename = sys.argv[1]
fcount = 1
cwd = os.getcwd()
cwd = cwd.split("/")
fname = filename

while os.path.exists(fname): 
  fname = "AUTO%d_"%fcount + filename
  fcount += 1
fw = open(fname,"w")
wstr = """# -*- coding: utf-8 -*-
# Google Code Jam %s
# %s %s

# --- modules ---
import sys

# --- const ---
DBG = True

# --- funcs ---
def ReadInts():
  line = sys.stdin.readline().rstrip().split()
  return map(int,line)

def dprint(dstr):
  if not DBG: return
  if dstr.__class__ == str:
    sys.stderr.write(dstr+"\\n")
  else:
    sys.stderr.write(str(dstr)+"\\n")

# --- main ---
"""%(cwd[-3],cwd[-2],cwd[-1])
fw.write(wstr)
fw.close()
