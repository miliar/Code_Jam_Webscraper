import sys
import pycosat
from collections import defaultdict

# Using https://pypi.python.org/pypi/pycosat

def trace(M,A,x,y,dx,dy):
    """Return if legal orientation for beam splitter"""
    while 1:
        if 0<=x<W and 0<=y<H:
            m=M[y][x]
            #print x,y,dx,dy,m
            if m=='|' or m=='-':
                return False
            elif m=='#':
                return True
            elif m=='/':
                dx,dy=-dy,-dx
                x+=dx
                y+=dy
                continue
                #return trace(M,A,x+dx,y+dy,dx,dy)
            elif m=='\\':
                dx,dy=dy,dx
                x+=dx
                y+=dy
                continue
                #return trace(M,A,x+dx,y+dy,dx,dy)
            else:
                assert m=='.'
                A.append((x,y))
                x+=dx
                y+=dy
                continue
                #return trace(M,A,x+dx,y+dy,dx,dy)
        else:
            return True

def go():
    """Return success and final map/None"""
    global R,C,W,H
    R,C = map(int,raw_input().split())
    H,W=R,C
    M=[]
    for r in range(R):
        M.append(list(raw_input().rstrip()))
    # Trace each beam splitter
    # Track for each empty square which beams can hit it
    # Will have at most 2 beam splitters per square

    empty = set()
    covered = set()

    D = {} # Map from splitter to pair of horz covered, vert covered

    E = {} # Map from beam variable to location

    B = defaultdict(list) # Map from empty cell to beam variables

    numbeams = 0
    for y in range(R):
        for x in range(C):
            m = M[y][x]
            if m=='-' or m=='|':
                # Try horizontal orientation
                horz = []
                badh = False
                for dx,dy in [[-1,0],[1,0]]:
                    if not trace(M,horz,x+dx,y+dy,dx,dy):
                        badh = True
                vert = []
                badv = False
                for dx,dy in [[0,1],[0,-1]]:
                    if not trace(M,vert,x+dx,y+dy,dx,dy):
                        #print 'badv found'
                        badv = True
                if badh and badv:
                    #print x,y
                    return False,None
                if badh:
                    # Force vertical
                    M[y][x]='|'
                    for c in vert:
                        covered.add(c)
                    continue
                if badv:
                    # Force horizontal
                    M[y][x]='-'
                    for c in horz:
                        covered.add(c)
                    continue
                D[ (x,y) ] = horz,vert
                numbeams+=1
                E[numbeams] = (x,y)
                for cell in horz:
                    B[cell].append(numbeams)
                for cell in vert:
                    B[cell].append(-numbeams)   
            elif m=='.':
                empty.add((x,y))
    #print 'here'
    cnf = []          
    for cell in empty:
        if cell in covered:
            continue
        if cell not in B:
            return False,None
        cnf.append(B[cell])
    #print cnf
    A = pycosat.solve(cnf)
    if A=="UNSAT" or A=="UNKNOWN":
        return False,None
    for v in A:
        if v>0:
            x,y = E[v]
            M[y][x] = '-'
        if v<0:
            x,y = E[abs(v)]
            M[y][x] = '|'
    return True,M           
    
#sys.stdin=open('datac.txt')
#sys.stdin=open('B-large.in')

T=input()
for t in range(1,T+1):
    success,M = go()
    if not success:
        print "Case #{}: IMPOSSIBLE".format(t)
    else:
        print "Case #{}: POSSIBLE".format(t)
        for row in M:
            print ''.join(row)
