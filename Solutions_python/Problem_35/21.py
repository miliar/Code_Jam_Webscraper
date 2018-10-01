#!/usr/bin/python
import sys, time, psyco
psyco.full()
rdl = sys.stdin.readline

def done(r):
    for i in r:
        if '_' in i: return False
    return True
        
def newlabel(r):
    chars = []
    for l in r:
        for c in l:
            if c != '_': chars.append(ord(c))
    return chr(max(chars)+1)

def empty(r):
    if done(r):
        return 0,0
    y = 0
    f = False
    for q in r:
        if '_' in q:
            x = q.index('_')
            break
        y += 1
    return y,x

def process(case):
    """precessing case #"""
    #[int(x) for x in sys.stdin.readline().split()]
    H, W = [int(x) for x in sys.stdin.readline().split()]
    m = []
    for dumb in xrange(H):
        m.append([int(x) for x in sys.stdin.readline().split()])
    r = []
    s = []
    for i in m:
        r.append(['_']*len(i))
        s.append([' ']*len(i))
    r[0][0] = 'a'
    y, x = 0,0
    label = 'a'
    flag = False
    while not done(r):
        #tmp = r[y][x]
        #r[y][x] = '*'
        #print '\n' + '\n'.join(' '.join(str(i)) for i in m)
        #print '\n' + '\n'.join(' '.join(i) for i in r)
        #r[y][x] = tmp
        #time.sleep(0.5)
        
        if flag:
            label = newlabel(r)
            flag = False        
        
        ny,nx = y,x
        # North
        if y>0 and m[y-1][x] < m[ny][nx]:
            # r[y-1][x] = label
            ny,nx = y-1,x
            
        # West
        if x>0 and m[y][x-1] < m[ny][nx]:
            # r[y][x-1] = label
            ny,nx = y,x-1
        
        # East
        if x+1<W and m[y][x+1] < m[ny][nx]:
            #r[y][x+1] = label
            ny,nx = y,x+1
        
        
        
        # South
        if y+1<H and m[y+1][x] < m[ny][nx]:
            #r[y][x+1] = label
            ny, nx = y+1,x
        
        
        
        if (ny, nx) == (y, x) and not done(r): # sink
            flag = True
            r[ny][nx] = label
            py, px = y,x
            y,x = empty(r)
        elif r[ny][nx] != '_':
            #flag = True
            r[y][x] = r[ny][nx]
            #y,x = empty(r)
            if r[py][px] == '_': y,x = py, px
            else: y,x = empty(r)
                         
        else:
            #r[y][x] = label
            py, px = y,x
            y,x = ny,nx
        #print y,x
    return 'Case #%d:\n'%case + '\n'.join(' '.join(i) for i in r)
                
                    
        


cases = int(rdl())
for case in xrange(1, cases+1):
    print process(case)
