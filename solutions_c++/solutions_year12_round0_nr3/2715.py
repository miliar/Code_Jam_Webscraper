inp = file('C-large-0.in')
out = file('C-large-0.out', 'w')
pairs = []
import time
start = time.time()
def getc(n, b):
    sst = str(n)*2
    total = 0
    ms = []
    for i in range(1, len(str(n))):
        mstr = sst[i:i+len(str(n))]
        m = int(mstr)
        if m>n and m<=b and len(str(m)) == len(mstr) and m not in ms:
            total+=1
            ms.append(m)
    return total

t = int(inp.readline())
for case in range(t):
    a,b = map(int, inp.readline().split())
    #print a,b
    total = 0
    for i in range(a, b):
        total += getc(i, b)
    out.write('Case #%d: '%(case+1)+str(total)+'\n')
    
print 'total: ', time.time() - start
