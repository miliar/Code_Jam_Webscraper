def flip(s):
    rev = ""
    for c in s:
        if c == "+":
            rev += "-"
        else:
            rev += "+"
    return rev
    
def findShortest(p,n):
    q = [(p,0)]
    seen = {p}
    while(q):
        u,c = q.pop()
        #print u
        #early vertex processing
        if u.count('+') == len(p):
            return str(c)
        for i in range(len(p)-n+1):
            newS = u[:i]+flip(u[i:i+n])+u[i+n:]
            #print(i,newS)
            if newS.count('+') == len(p):
                return str(c+1)
            if newS not in seen:                
                q.insert(0,(newS,c+1))
                seen.add(newS)
        #late vertex processing
    return "IMPOSSIBLE"
    
l = int(raw_input())
for x in range(l):
    p,n = raw_input().split()
    n = int(n)
    print "Case #"+str(x+1)+": "+findShortest(p,n)
    