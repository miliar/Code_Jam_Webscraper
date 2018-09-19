import sys

args = sys.argv

if len(args) < 2:
    print 'small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

# No change before this

cache = map(int, open('cache_small.txt').read().split())

def int_row():
    return map(int, raw_input().split())

def solve():
    A, B = int_row()
    a = int(ceil(sqrt(A)))
    b = int(sqrt(B))
    count = 0
    for c in cache:
        if c > b:
            break
        if a <= c and c <= b:
            count += 1
    return str(count)

from math import sqrt, ceil

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')

c_out = open('cache.txt', 'w')
for c in cache:
    c_out.write(str(c) + ' ')

# No change after this

out.close()
