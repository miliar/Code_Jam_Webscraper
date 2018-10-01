# Solution to "Stable Neigh-bors" for Google Code Jam 2017
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            yield [int(x) for x in f.readline().split()]

def solve(n, r, o, y, g, b, v):
    if max(r,o,y,g,b,v) > n/2:
        return 'IMPOSSIBLE'
    if (b < o) or (r < g) or (y < v):
        return 'IMPOSSIBLE'
    if ((b == o) and (o > 0)) and ((g > 0) or (v > 0)):
        return 'IMPOSSIBLE'
    if ((g == r) and (g > 0)) and ((o > 0) or (v > 0)):
        return 'IMPOSSIBLE'
    if ((v == y) and (v > 0)) and ((o > 0) or (g > 0)):
        return 'IMPOSSIBLE'
    result = ""
    if (o > 0): b -= o + 1
    if (g > 0): r -= g + 1
    if (v > 0): y -= v + 1
    l = [[b, 'B'], [r, 'R'], [y, 'Y']]
    l.sort(reverse=True)
    for _, col in l:
        if col == 'B' and o > 0:
            result += 'B'
            result += 'OB'*o
        elif col == 'R' and g > 0:
            result += 'R'
            result += 'GR'*g
        elif col == 'Y' and v > 0:
            result += 'Y'
            result += 'VY'*v
    if l[2][0] < 0:
        return result[:-1]
    if len(result) > 0 and result[-1] == l[0][1]:
        l[0][0] += 1
        result = result[:-1]   
    endLen = n - len(result)
    halfEndLen = (endLen+1)/2
    endBit = l[0][1]*l[0][0]
    midLen = halfEndLen - l[0][0]
    endBit += l[1][1]*midLen
    newEnd = ""
    for x in range(l[1][0]-midLen):
        newEnd += endBit[x]+l[1][1]
    for x in range(l[1][0]-midLen,l[1][0]-midLen+l[2][0]):
        newEnd += endBit[x]+l[2][1]
    t = l[1][0]-midLen+l[2][0]
    if len(endBit) > t + 1:
        return 'IMPOSSIBLE'
    if len(endBit) == t + 1:
        newEnd += endBit[t]
    return result + newEnd

with open(sys.argv[2], 'w') as f:
    for num, args in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %s\n"%(num+1, solve(*args)))
