import math

# def half(n):
#     x = 1
#     while n != 1:
#         n = n / 2
#         x += 1
#     return x

def half(n):
    if n == 0:
        return 0
    else:
        return math.ceil(math.log(n, 2)) + 1

def test(L, P, C):
    n = L * C
    x = 1
    while n < math.ceil(P/float(C)):
        n = n * C
        x += 1
    return x

def solve(L, P, C):
    if L * C >= P:
        return 0
    else:
        return half(test(L, P, C) + 1) - 1

if __name__ == '__main__':
    T = input()
    for x in xrange(T):
        L, P, C = (int(x) for x in raw_input().split())
        y = solve(L, P, C)
        print 'Case #%d: %d' % ((x + 1), y)
