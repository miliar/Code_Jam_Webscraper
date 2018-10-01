
el = ['1', 'i', 'j', 'k']
e = {'1':0, 'i':1, 'j':2, 'k':3}
m = [1, 'i', 'j', 'k', 'i', '-1', 'k', '-j', 'j', '-k', '-1', 'i', 'k', 'j', '-i', '-1']

def mult(x, y):
    neg = False
    if x[0]=='-':
        x = x[1]
        neg = not neg
    if y[0]=='-':
        y = y[1]
        neg = not neg
    res = m[e[x]*4 + e[y]]
    if neg:
        if res[0]=='-':
            return res[1]
        else:
            return '-'+res
    else:
        return res

def dijkstra(s):
    l = len(s)
    start = 0
    end = l
    while 1:
        val = s[0]
        i = 1
        while val!='i' and i<l:
            val = mult(val, s[i])
            i += 1
        if val != 'i':
            return "NO"
        j = i
        val = s[l-1]
        k = l-2
        while val!='k' and k>j:
            val = mult(s[k], val)
            k -= 1
        if val != 'k':
            return "NO"
        val = s[j]
        while j!=k:
            j += 1
            val = mult(val, s[j])
        if val == 'j':
            return "YES"
        else:
            return "NO"

def dijk(l, x, s):
    if l*x<=3:
        if s =="ijk":
            return "YES"
        else:
            return "NO"
    if s in el:
        return "NO"
    st = ""
    for i in xrange(x):
        st = st + s
    ret = dijkstra(st)
    return ret

if __name__ == "__main__":
    fi = open('inp', 'r')
    line = fi.readline()
    #print line
    T = int(line)
    fo = open('out.txt', 'w')
    for i in xrange(T):
        line = fi.readline()
        l = line.split(' ')
        L = int(l[0])
        X = int(l[1])
        #print L, X
        line = fi.readline().strip()
        #print line
        out = "Case #"+str(i+1)+": "+dijk(L, X, line)+'\n'
        print out
        fo.write(out)

    fo.close()
    fi.close()

