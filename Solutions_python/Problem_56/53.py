
def solve(N,K):
    a=[raw_input() for x in range(N)]
    w=len(a[0])
    blue=red=False
    for i in range(len(a)):
        a[i] = a[i].replace(".","").rjust(w,'.') 
    for x in range(w):
        for y in range(N):
            for d in (1,0),(0,1),(1,1),(1,-1):
                try:
                    s="".join([a[y+d[1]*k][x+d[0]*k] for k in range(K)])
                except:
                    continue
                if s=="B"*K: blue=True
                if s=="R"*K: red=True
    if red and blue: return "Both"
    if red: return "Red"
    if blue: return "Blue"
    return "Neither"
                
T=input()
for c in range(T):
    N,K=map(int,raw_input().split())
    result=solve(N,K)
    print "Case #%s: %s"%(c+1, result)
