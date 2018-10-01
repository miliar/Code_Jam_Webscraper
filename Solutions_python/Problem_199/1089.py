# -*- coding: utf-8 -*-
def solve01(t):
    sk = t.split(' ')
    s = sk[0]
    k = int(sk[1])  
    f = 0
    while len(s) > k:
        if s[0] == '0':
            f += 1
            news = ''
            for i in range(1,k):
                news += str(1-int(s[i]))
            s = news + s[k:]
        else:
            s = s[1:]
    if len([c for c in s if c == s[0]]) == len(s):
        if s[0]=='0':
            f += 1
    else:
        f = 'IMPOSSIBLE'
    return str(f)

def solve(s):
    return solve01(s.replace('+','1').replace('-','0'))

f = open('A-large.in','r')
fo = open('result.txt','w')
t = int(f.readline())
for ti in range(t):
    s = f.readline()
    r = solve(s)
    rs = "Case #%d: %s\n" % (ti+1, r)
    print(rs)
    fo.write( rs )
fo.close()
f.close()
