import sys
import time
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a) + "\n")
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(f): return map(f,raw_input().split())
def alloc(size, default = 0): return [default] * size
def dig(c): return ord(c) - 48

t00 = time.clock()

        
def solve(N,K,B,T,Xlist,Vlist):
    cnt = 0
    lastPos = []
    for i in xrange(N):
        lastPos.append(Xlist[i] + Vlist[i] * T)
    for i in xrange(N-1,-1,-1):
        if lastPos[i] >= B:
            cnt += 1
            del(lastPos[i])
        else:
            break
    dbg(lastPos)
    if cnt >= K: return 0
    reaches = []
    for i,l in enumerate(lastPos):
        if l >= B: reaches.append(i)
    dbg(reaches)
    reaches.reverse()
    res = 0
    llp = len(lastPos)
    k=0
    while cnt < K and len(reaches) > 0:
        i = reaches.pop(0)
        res += (llp-1)-i-k
        cnt += 1
        k += 1
    if cnt >= K: return res
    else: return -1

    

for t in range(readint()):
    t0 = time.clock()
    dbg("Test #%d:" % (t+1))
    N,K,B,T = readarray(int)
    dbg("N %d K %d B %d T %d" % (N,K,B,T))
    Xlist = readarray(int)
    Vlist = readarray(int)
    dbg(str(Xlist))
    dbg(str(Vlist))
    ans = solve(N,K,B,T,Xlist,Vlist)
    print "Case #%d:" % (t+1),
    if ans < 0:
        print "IMPOSSIBLE"
    else:
        print ans
    dbg("time %.2f sec" % (time.clock() - t0))

dbg("total time %.2f sec" % (time.clock() - t00))
