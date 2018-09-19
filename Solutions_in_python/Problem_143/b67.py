import itertools


dictK = {}
def applyAnd(a, b):
    a = bin(a)[2:]
    b = bin(b)[2:]
    t = max([len(a), len(b)])
    a = a.zfill(t)
    b = b.zfill(t)
    res = ''
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            res += '1'
        else:
            res += '0'
    return int(res, 2)

def doit(A, B, K):
    res = 0
    for i in range(A):
        for j in range(B):
            if (i, j) not in dictK:
                x = applyAnd(i, j)
                dictK[(i, j)] = x
                dictK[(j, i)] = x
            if dictK[(i, j)] < K:
                res += 1
    return res

def doit2(A, B, K):
    res = 0
    gen = itertools.permutations(range(max(A, B)))
    for i in gen:
        if i[0] < A and i[1] < B:
            if applyAnd(i[0], i[1]) < K:
                res += 1
    return res

res = []
for i in range(input()):
    res.append(doit(*map(int, raw_input().split())))

for i in range(len(res)):
    print "Case #" + str(i+1) + ': ' + str(res[i])
