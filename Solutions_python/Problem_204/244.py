import sys
import math

t = int(sys.stdin.readline().strip())
for ti in xrange(t):
    line = sys.stdin.readline().split()
    n = int(line[0])
    p = int(line[1])
    r = map(int, sys.stdin.readline().split())
    q = []
    for ni in xrange(n):
        line = map(int, sys.stdin.readline().split())
        line.sort()
        q.append(line)

    k = []
    for ni in xrange(n):
        k.append([])
        for pi in range(p):
            min_k = int(math.ceil(q[ni][pi] / (1.1 * r[ni])))
            max_k = int(math.floor(q[ni][pi] / (0.9 * r[ni])))
            if max_k >= min_k:
                s = set(xrange(min_k, max_k + 1))
                k[ni].append((s, min_k, max_k))

    kis = [0] * n
    klens = [len(ke) for ke in k]

    solved = False
    for kl in klens:
        if kl == 0:
            print 'Case #%d: 0' % (ti + 1)
            solved = True
            break
    if solved:
        continue

    result = 0
    while True:
        s = k[0][kis[0]][0]
        for ni in xrange(n):
            s = s.intersection(k[ni][kis[ni]][0])
        if s:
            result += 1
            solved = False
            for ni in xrange(n):
                kis[ni] += 1
                if kis[ni] >= klens[ni]:
                    solved = True
                    break
            if solved:
                break
            continue
        min_i = 0
        min_v = k[0][kis[0]][2]
        for ni in xrange(n):
            if k[ni][kis[ni]][2] < min_v:
                min_v = k[ni][kis[ni]][2]
                min_i = ni
        kis[min_i] += 1
        if kis[min_i] >= klens[min_i]:
            break

    print 'Case #%d: %d' % (ti + 1, result)
        
