from itertools import groupby

f = open('input.in')
g = open('output', 'w')

T = int(f.readline()[:-1])

def getLetters(S) :
    res = []
    for s in S :
        if len(res) ==0 or s != res[-1] : res.append(s)
    return tuple(res)

def getCount(S) :
    return [len(list(l)) for k, l in groupby(S)]

for case in range(T) :
    N = int(f.readline()[:-1])
    S = [f.readline()[:-1] for i in range(N)]
    L = [getLetters(s) for s in S]
    if len(set(L)) != 1 : res = 'Fegla Won'
    else :
        L = [getCount(s) for s in S]
        L = zip(*L)
        res = 0
        for l in L :
            m = float(sum(l))/len(l)
            minmove = min([sum([abs(i-t) for i in l]) for t in range(int(m), int(m) + 2)])
            res += minmove
    output = 'Case #' + str(case+1) + ': ' + str(res)
    g.write(output + '\n')
    print output

f.close()
g.close()
