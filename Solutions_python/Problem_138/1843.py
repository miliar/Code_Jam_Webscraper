import sys

def getf(func):
    return func(sys.stdin.readline().strip())
def getl(func):
    return map(func, sys.stdin.readline().strip().split())


def proc(Nl, Kl):
    n = len(Nl)
    nc = 0
    np = 0
    kp = 0
    ans = 0
    
    while kp < n:
        #print Nl[np], Kl[kp], nc, ans
        if np > n-1:
            ans += 1
            kp += 1
        elif Nl[np] < Kl[kp]:
            nc += 1
            np += 1
        else:
            if nc > 0:
                ans += 1
                nc -= 1
            kp += 1
    return ans


for i in range(getf(int)):
    n = getf(int)
    Nl = getl(float)
    Kl = getl(float)
    Nl.sort()
    Kl.sort()
    
    print "Case #"+str(i+1)+":",proc(Kl, Nl), n - proc(Nl, Kl)

