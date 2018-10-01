from collections import defaultdict
import copy

def solve3(hd, ad, hk, ak, b, d):
    visited = set()
    z = 0
    orig_hd = hd
    q = [(0, hd, ad, hk, ak, b, d)]
    while len(q) > 0:
        z += 1
        (turn, hd, ad, hk, ak, b, d) = q.pop(0)
        if (hd, ad, hk, ak, b, d) in visited:
            continue
        visited.add((hd, ad, hk, ak, b, d))

        if turn > 1000: continue
#         if z > 1000000:break
#         print('-=-=-before')
#         print(q)
        if hk <= 0:
            return turn
        if hd <= 0:
            continue
        q.append((turn + 1, hd - ak, ad, hk - ad, ak, b, d)) # attack
        if b > 0:
            q.append((turn + 1, hd - ak, ad + b, hk, ak, b, d)) # buff
        if hd < orig_hd:
            q.append((turn + 1, orig_hd - ak, ad, hk, ak, b, d)) # cure
        if d > 0:
            new_ak = max([0, ak - d])
            q.append((turn + 1, hd - new_ak, ad, hk, new_ak, b, d)) # debuff
#         print('-=-=-after')
#         print(q)
    return 'IMPOSSIBLE'

with open('out3', 'wt') as o:
    lines = [l.strip() for l in open('C-small-attempt0.in').readlines()]
    numTests = int(lines[0])
    nextTestLine = 1
    testsCounter = 0
    while testsCounter < numTests:
        testsCounter += 1
        hd, ad, hk, ak, b, d = [int(i) for i in lines[nextTestLine].split()]
        testLines = lines[nextTestLine + 1 : nextTestLine + 1 + n + 1]
        nextTestLine += 1
        print('\nsolving: %s' % ([(hd, ad, hk, ak, b, d)]))
        res = solve3(hd, ad, hk, ak, b, d)
        result = 'Case #%d: %s' % (testsCounter, res)
        print(result)
        _ = o.write(result + '\n')

