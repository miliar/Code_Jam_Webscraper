def solve(L, X, word):
    word = map(lambda w: quatMap[w], word)
    wn = len(word)
    pa = 0
    ijk = 1
    for x in xrange(0, X):
        for w in word:
            pa = quatMulMap[pa, w]
            #print pa, 
            if pa == ijk:
                pa = 0
                if ijk == 1: ijk = 2
                elif ijk == 2: ijk = 3
                elif ijk == 3: ijk = 0
    #print 
    return ijk == 0 and pa == 0

quatN = 4
quatArr = ['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k']
quatMap = {}
quatMul = [
           ['1',  'i',  'j',  'k'],
           ['i', '-1',  'k', '-j'],
           ['j', '-k', '-1',  'i'],
           ['k',  'j', '-i', '-1']
           ]
quatMulMap = {}

for i in xrange(0, len(quatArr)):
    quatMap[quatArr[i]] = i
for i in xrange(0, quatN):
    for j in xrange(0, quatN):
        quatMulMap[i, j] = quatMap[quatMul[i][j]]
        quatMulMap[i+4, j] = (quatMap[quatMul[i][j]] + 4) % 8
        quatMulMap[i, j+4] = (quatMap[quatMul[i][j]] + 4) % 8
        quatMulMap[i+4, j+4] = quatMap[quatMul[i][j]]
#print quatMulMap

T = int(raw_input())
for t in xrange(1, T+1):
    line = raw_input()
    L, X = tuple(map(lambda s: int(s), line.split()))
    word = raw_input()
    #print L, X, word
    rc = solve(L, X, word)
    print "Case #{0}: {1}".format(t, 'YES' if rc else 'NO')