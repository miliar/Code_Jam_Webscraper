#!/usr/bin/env python
import sys
ls = sys.stdin.readlines()
NC = int(ls[0])
ls = ls[1:]

cache = {}
def feasible(c, state):
    if (c, state) in cache:
        return cache[(c, state)]
    def R(ans):
#        print c, state, ans
        cache[(c, state)] = ans
        return ans
    if c == nc:
        return R('.' not in state)
    bs = []
    for r in range(nr):
        if g[r][c] in ('-', '|'):
            if state[r] == '-':
                return R(False)
            bs.append(r)
        elif g[r][c] == '.' and state[r] == '|':
            return R(False)
        elif g[r][c] == '#' and state[r] == '.':
            return R(False)

    for bm in range(2**len(bs)):
        newstate = [x for x in state]
        for r in range(nr):
            if g[r][c] == '#':
                newstate[r] = '#'
            if g[r][c] == '.' and state[r] == '#':
                newstate[r] = '.'
        skip = False
        for i in range(len(bs)):
            if bm & (2**i):
                if state[bs[i]] == '.':
                    skip = True
                    continue
                for r in range(bs[i]+1, nr):
                    if g[r][c] == '#':
                        break
                    if g[r][c] in ('-', '|'):
                        skip = True
                        break
                    if state[r] != '.':
                        newstate[r] = '#'
                for r in range(bs[i]-1, -1, -1):
                    if g[r][c] == '#':
                        break
                    if g[r][c] in ('-', '|'):
                        skip = True
                        break
                    if state[r] != '.':
                        newstate[r] = '#'
                if skip:
                    continue
                newstate[bs[i]] = '|'
            else:
                if newstate[bs[i]] == '|':
                    skip = True
                else:
                    newstate[bs[i]] = '-'
        if skip:
            continue
        if feasible(c + 1, "".join(newstate)):
            return R(True)
    return R(False)

def rpath(c, state):
    if c == nc:
        return []
    bs = []
    for r in range(nr):
        if g[r][c] in ('-', '|'):
            bs.append(r)

    for bm in range(2**len(bs)):
        newstate = [x for x in state]
        for r in range(nr):
            if g[r][c] == '#':
                newstate[r] = '#'
            if g[r][c] == '.' and state[r] == '#':
                newstate[r] = '.'
        skip = False
        for i in range(len(bs)):
            if bm & (2**i):
                if state[bs[i]] == '.':
                    skip = True
                    continue
                for r in range(bs[i]+1, nr):
                    if g[r][c] == '#':
                        break
                    if g[r][c] in ('-', '|'):
                        skip = True
                        break
                    if state[r] != '.':
                        newstate[r] = '#'
                for r in range(bs[i]-1, -1, -1):
                    if g[r][c] == '#':
                        break
                    if g[r][c] in ('-', '|'):
                        skip = True
                        break
                    if state[r] != '.':
                        newstate[r] = '#'
                if skip:
                    continue
                newstate[bs[i]] = '|'
            else:
                if newstate[bs[i]] == '|':
                    skip = True
                else:
                    newstate[bs[i]] = '-'
        if skip:
            continue
        if feasible(c + 1, "".join(newstate)):
            path = rpath(c+1, "".join(newstate))
            for i in range(len(bs)):
                path.append((bs[i], c, '|' if (bm & (2**i)) else '-'))
            return path

for C in range(NC):
    nr, nc = [int(x) for x in ls[0].split()]
    g = ls[1:1+nr]
    ls = ls[1+nr:]
#    print g

    cache = {}
    f = feasible(0, "#" * nr)
    print "Case #%d: %sPOSSIBLE" % (C + 1, "" if f else "IM")
    if f:
        path = rpath(0, "#" * nr)
        ng = []
        for r in range(nr):
            ng.append([])
            for c in range(nc):
                ng[r].append(g[r][c])
        for p in path:
            ng[p[0]][p[1]] = p[2]
        for r in range(nr):
            print "".join(ng[r])
