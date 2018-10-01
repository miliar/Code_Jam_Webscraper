# Using satispy from
# https://pypi.python.org/pypi/satispy
# (BSD license)
# and Debian package minisat

from sys import stdin
from satispy import Variable, Cnf
from satispy.solver import Minisat                                  

def getstrings(): return [x for x in stdin.readline().strip().split()]
def getints(): return [int(x) for x in stdin.readline().strip().split()]
def getfloats(): return [float(x) for x in stdin.readline().strip().split()]

# Finds reachable set from p=(r,c) in direction d=(1,0), (-1,0), (0,1) or (0,-1)
# (d=entrance direction)
def fire(R,C,grid,p,d):
  seen=set()
  (r,c)=p
  while 1:
    (r,c)=(r+d[0],c+d[1])
    if r<0 or r>=R or c<0 or c>=C: break
    if (r,c)+d in seen: break
    seen.add((r,c)+d)
    if grid[r][c] in ['-','|','#']: break
    if grid[r][c]=='/': d=(-d[1],-d[0])
    if grid[r][c]=='\\': d=(d[1],d[0])
  rs=set()
  for x in seen: rs.add(x[:2])
  return rs

def twofire(R,C,grid,p,d):
  return fire(R,C,grid,p,d).union(fire(R,C,grid,p,(-d[0],-d[1])))

def thing(R,C,grid):
  #print R,C;print grid;print
  guns=set()
  clauses=set()
  for r in range(R):
    for c in range(C):
      if grid[r][c] in ['|','-']: guns.add((r,c))
      if grid[r][c]=='.': clauses.add((r,c))
  assigns={}
  vars=[]
  for r in range(R):
    for c in range(C):
      if grid[r][c] not in ['-','|']: continue
      bad=set()
      for d in [(1,0),(0,1)]:
        reach=twofire(R,C,grid,(r,c),d)
        if reach.intersection(guns): bad.add(d)
      if len(bad)==2: print "IMPOSSIBLE";return
      if len(bad)==1:
        for d in bad: pass
        d=(d[1],d[0])
        reach=twofire(R,C,grid,(r,c),d)
        assigns[(r,c)]=d
        for p in reach: clauses.discard(p)
      if len(bad)==0:
        vars.append((r,c,twofire(R,C,grid,(r,c),(1,0)),twofire(R,C,grid,(r,c),(0,1))))
  exp={}# map from clauses to list of (possibly negated) variables that will satisfy clause
  varlist={}
  for (r,c,s0,s1) in vars:
    v=Variable((r,c));varlist[(r,c)]=v
    for p in s0:
      if p in clauses: exp.setdefault(p,[]).append(v)#;print r,c,p,'|'
    for p in s1:
      if p in clauses: exp.setdefault(p,[]).append(-v)#;print r,c,p,'-'
  v=Variable('dummy')
  texp=v|-v# Dunno how to get 'true'
  for p in clauses:
    if p not in exp: print "IMPOSSIBLE";return
    l=exp[p]
    assert len(l)<=2
    if len(l)==1: texp=texp & l[0]
    else: texp=texp & (l[0] | l[1])
  solution = solver.solve(texp)
  if not solution.success: print "IMPOSSIBLE";return
  for (r,c,s0,s1) in vars:
    v=varlist[(r,c)]
    if solution[v]: assigns[(r,c)]=(1,0)
    else: assigns[(r,c)]=(0,1)
  #print assigns
  print "POSSIBLE"
  lgrid=[list(grid[r]) for r in range(R)]
  for (r,c) in assigns:
    if assigns[(r,c)]==(1,0): lgrid[r][c]='|'
    else: lgrid[r][c]='-'
  for r in range(R):
    print ''.join(lgrid[r])

solver = Minisat()
T=int(stdin.readline())
for case in range(1,T+1):
  [R,C]=getints()
  grid=[stdin.readline().strip() for i in xrange(R)]
  print "Case #%d:"%case,;thing(R,C,grid)
