def colors2(l):
    n = sum(l)
    string = 'ROYGBV'
    #dic = {string[i]: l[i] for i in range(sum(l))}
    for j in l:
        if j >n*1.0/2:
            return "IMPOSSIBLE"
    jj = max(l)
    if l.index(jj) ==0:
        answer = colors(l)
        return answer
    if l.index(jj)==2:
        l[0], l[2] = l[2], l[0]
        answer = colors(l)
        final = ''
        for j in answer:
            if j == 'R':
                final += 'Y'
            if j == 'Y':
                final += 'R'
            if j == 'B':
                final += 'B'
        return final
        
    if l.index(jj)==4:
        l[0], l[4] = l[4], l[0]
        answer = colors(l)
        final = ''
        for j in answer:
            if j == 'R':
                final += 'B'
            if j == 'Y':
                final += 'Y'
            if j == 'B':
                final += 'R'
        return final
    
def colors(l):
    n = sum(l)
    string = 'ROYGBV'
    #dic = {string[i]: l[i] for i in range(sum(l))}
    for j in l:
        if j >n*1.0/2:
            return "IMPOSSIBLE"
    else:
        r = ''
        temp1 = max(l)
        r += string[l.index(temp1)]
        l[l.index(temp1)] -= 1
        for k in range(n-1):
            #print l
            temp1 = string.index(r[-1])
            #print temp1, string.index(r[-1])
            p = [l[a] if a!=temp1 else 0 for a in range(len(l))]
            temp2 = max(p)
            temp3 = p.index(temp2)
            #print temp2, temp3
            l[temp3] -= 1
            r += string[temp3]
            #print r, l, p
    return r

f = [line.rstrip() for line in open('/Users/roshil/Desktop/B-small-attempt4.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for j in range(1, testcases+1):
    m = [int(a) for a in f[line].split()]
    line += 1
    m = m[1:]
    ans = colors2(m)
    #print ans
    out.write("Case #"+str(j)+": "+str(ans) + "\n")
out.close()
            