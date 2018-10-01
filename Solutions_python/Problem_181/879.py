import sys, string
import time

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()
for t in range(T):
    S = sys.stdin.readline().strip()
    
    #~ if t != 3: continue
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    
    w = S[0]
    for i,ch in enumerate(S[1:]):
        # front or back?
        #~ print i,ch
        remain = S[i+1:]
        remain = [c for c in remain] + [0]
        #~ print i, ch, w[0]
        if ch >= w[0]:#  max(remain) >= ord(ch):
            w = ch + w
        else:
            w = w + ch
        #~ print w
    
    print w
