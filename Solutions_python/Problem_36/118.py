with open("C-large.in") as f:
    n = int(f.readline().strip())
    strs = [f.readline().strip() for i in range(n)]
    
memoize = {}
def sb(s,rest,p):
    if memoize.has_key(rest):
         cc = 0
         for pos,cnt in sorted(memoize[rest]):
             if pos >= p:
                 cc += cnt
         if cc >0: return cc
        

    count = 0
    if rest == '':
        return 1
    
    if len(s) < len(rest):
        return 0
    
    l = rest[0]
    
    for (i,c) in enumerate(s):
        if c == l:
            e = sb(s[i+1:],rest[1:],p+1)
            count += e
            if e == 0:
                break
            else:
                if memoize.has_key(rest):
                    memoize[rest].append((p,e))
                else:
                    memoize[rest] = [(p, e)]
        p += 1
            
    return count
    
out = open("out-large.txt", "w")
for (i,s) in enumerate(strs):
    memoize = {}
    count = sb(s,"welcome to code jam",0)
    print >> out, "Case #%d: %s" % (i+1,str(count)[-4:].zfill(4))
