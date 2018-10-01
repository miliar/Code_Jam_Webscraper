#!/usr/bin/python
import sys

def lstr(l):
  rs = '['
  n = len(l)
  cnt = 0
  for i in l:
    rs += i
    if cnt != n - 1:
      rs += ', '
    cnt += 1
  return rs + ']'
  
def io():
  with open('input', 'r') as inf:
    with open('output','w') as of:
      lno = 0
      for l in inf:
        lno += 1 
        # Code begins here
        if lno > 1:
          ls = l.split()
          i = pb(ls, 0)
          i = po(ls, i)
          o = solve(ls[i+1], int(ls[i]))
          ol = "Case #%d: " % (lno - 1,) + lstr(o)
          of.write(str(ol) + '\n')
bd = {}
od = {}
def pb(l, i):
  global bd
  bd = {}
  c = int(l[i])
  it = i + 1
  while it <= i + c:
    cs = l[it]
    c1, c2, c3 = cs[0], cs[1], cs[2]
    if bd.get(c1) != None:
      bd[c1].append([c2, c3])
    else:
      bd[c1] = [[c2, c3]]
    if bd.get(c2) != None:
      bd[c2].append([c1, c3])
    else:
      bd[c2] = [[c1, c3]]
    it = it + 1

  return it 
  
def po(l,i):
  global od
  od = {}
  c = int(l[i])
  it = i + 1
  while it <= i + c:
    cs = l[it]
    c1, c2 = cs[0], cs[1]
    if od.get(c1) != None:
      od[c1].append(c2)
    else:
      od[c1] = [c2]
    if od.get(c2) != None:
      od[c2].append(c1)
    else:
      od[c2] = [c1]
    it = it + 1
  return it

def checko(s,c):
  cod = od.get(c)
  if cod != None:
    for co in cod:
      o = s.get(co)
      if o != None:
        return True
  return False

def checkc(c,cp):
  pc = bd.get(c)
  if pc != None:
    for p in pc:
      if p[0] == cp:
        return p[1]
  return ''
  
def solve(st, ln):
  ret = []
  s = {}
  i=0
  while i < ln:
    if len(ret) == 0:
      ret.append(st[i])
      s[st[i]] = 1
    else:
      c = st[i]
      cp = ret[-1]
      cc = checkc(c,cp)
      if cc != '':
        cd = ret.pop()
        s[cd] =  s[cd] - 1
        if s[cd] == 0:
          del s[cd]
        ret.append(cc)
      else:
        if checko(s,c):
          ret = []
          s.clear()
        else:
          ret.append(c)
          if s.get(c) != None:
            s[c] += 1
          else:
            s[c] = 1
    i += 1
  
  return ret


if __name__ == "__main__":
  io()



