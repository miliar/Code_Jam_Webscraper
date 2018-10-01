import sys
t = [['1','i','j','k'],
     ['i','-1','k','-j'],
     ['j','-k','-1','i'],
     ['k','j','-i','-1']]
d = {'1':0,'i':1,'j':2,'k':3}
def multi(a,b):
    s = 0
    if len(a) == 2:
        s += 1
        a = a[1]
    if len(b) == 2:
        s += 1
        b = b[1]
    if s % 2 == 0:
        return t[d[a]][d[b]]
    ans = t[d[a]][d[b]]
    if len(ans) == 2:
        return ans[1]
    return '-'+ans
  
ca = int(sys.stdin.readline())
for nu in range(ca):
    l,x = sys.stdin.readline().strip().split(' ')
    l = int(l)
    x = int(x)
    data = sys.stdin.readline()
    a = '1'
    for i in range(l):
        a = multi(a,data[i])
    b = '1'
    for i in range(x):
        b = multi(b,a)

    if not(b == '-1'):
        print 'Case #%d: NO' %(nu+1)
        continue
    w1 = {'i':-1,'j':-1,'k':-1}
    w = 0
    a = '1'
    for i in range(x):
        for j in range(l):
            a = multi(a,data[j])
            if len(a) == 1 and a != '1' and w1[a] < 0:
                w1[a] = w
            w += 1
    w2 = {'i':-1,'j':-1,'k':-1}
    w = l * x - 1
    a = '1'
    for i in range(x): 
        for j in range(l):
            a = multi(data[l-j-1],a)
            if len(a) == 1 and a != '1' and w2[a] < 0:
                w2[a] = w
            w -= 1
    if w1['i'] < w2['k']:
        print 'Case #%d: YES' %(nu+1)
        continue
    print 'Case #%d: NO' %(nu+1) 
