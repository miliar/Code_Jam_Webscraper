## Theme Park, Q3
## David Horscroft

def fillCoaster(_k, _G):
    j = _k
    full = False
    result = []
   # print _G
   # print k
    while not full:
        if _G[0] > j:
            full = True
        else:
            j -= _G[0]
            result.append(_G.pop(0))
        if not _G:
            full = True
    return result

def add(customers):
    result = 0
    for j in xrange(len(customers)):
        result += customers[j]
    return result
            

## Reading File

f = open(raw_input('Filename: '), 'r')
T = -1
b = True
R = []
k = []
N = []
G = []

for ln in f:
    if T == -1:
        T = int(ln)
    elif b:
        R.append(int(ln.split(' ')[0]))
        k.append(int(ln.split(' ')[1]))
        N.append(int(ln.split(' ')[2]))
        b = False
    else:
        tGroup = []
        for i in ln.split(' '):
            tGroup.append(int(i))
        G.append(tGroup)
        b = True

## Calculations

for x in xrange(T):
    inc = 0
    for y in xrange(R[x]):
        cust = fillCoaster(k[x], G[x])
        inc += add(cust)
        for z in xrange(len(cust)):
            G[x].append(cust[z])
    print 'Case #' + str(x+1) + ': ' + str(inc)
