# -*- coding: utf-8 -*-
# Google Code Jam 2009
# Round1B A

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
    sys.stderr.write(dstr+"\n")
  else:
    sys.stderr.write(str(dstr)+"\n")

def ReadStrTree(L):
  line = ""
  for l in xrange(L):
    line += sys.stdin.readline().rstrip()
  Root = ReadTree(line,0)
  return Root

def ReadTree(line,st):
  line_len = len(line)
  idx = st
  tree = []
  while idx < line_len and line[idx] != "(": idx += 1
  if line_len == idx: return (None,idx)
  #weight
  idx += 1
  while line[idx] == " ": idx += 1
  st = idx
  while idx < line_len and line[idx] != " " and line[idx] != ")":  idx += 1
  en = idx
  tree.append(float(line[st:en]))
  while idx < line_len and line[idx] == " ": idx += 1
  if idx == line_len:
    return (tree,idx)
  elif line[idx] == ")":
    return (tree,idx+1)
  else:
    # feature
    st = idx
    while line[idx] != " ": idx += 1
    en = idx
    tree.append(line[st:en])
    # sub tree
    sub1 = ReadTree(line,idx+1)
    sub2 = ReadTree(line,sub1[1])
    if sub1[0] != None:
      tree.append(sub1[0])
    if sub2[0] != None:
      tree.append(sub2[0])
    idx = sub2[1]
    while idx < line_len and line[idx] != ")": idx += 1
    if idx == line_len: idx -= 1
    return (tree,idx+1)

def CalcProb(animals,root):
  for alst in animals:
    name,n,feats = alst
    ret = 1
    cur = root
    while 1:
      ret *= cur[0]
      if len(cur) == 1: break
      else:
        if cur[1] in feats:
          cur = cur[2]
        else:
          cur = cur[3]
    print "%.7f"%ret
      

# --- main ---
N = ReadInts()[0]
for prob in xrange(1,N+1):
  L = ReadInts()[0]
  root = ReadStrTree(L)[0]
  A = ReadInts()[0]
  animals = []
  for a in xrange(A):
    line = sys.stdin.readline().rstrip().split()
    name = line[0]
    n = int(line[1])
    feats = line[2:]
    animals.append((name,n,feats))
  print "Case #%d:"%prob
  CalcProb(animals,root)
