import math

def is_top(x):
    x = int(x)
    while x > 2:
        x >>= 1
    return (x & 1) == 0

def to_binary(x):
    bits = []
    while x:
        bits.append(x & 1)
        x >>= 1
    return bits[::-1]

def from_binary(bits):
    out = 0
    for b in bits:
        out = (2*out) + int(b)
    return out

def lower_idx(n):
    bits = to_binary(n)
    bits.pop(0)
    bits.pop(0)
    return from_binary([1] + bits)

def even(x):
    return (x & 1) == 0

def floor2(n):
    return int(n / 2.0)

def ceil2(n):
    return int(math.ceil(n / 2.0))

def f(n, k):
    def t(i):
        if i < 1:
            return n
        if i == 1:
            return ceil2(n - 1)
        parent_idx = lower_idx(i)
        parent = t(parent_idx) if is_top(i) else b(parent_idx)
        return ceil2(parent - 1)

    def b(i):
        if b < 1:
            return n
        if i == 1:
            return floor2(n - 1)
        parent_idx = lower_idx(i)
        parent = t(parent_idx) if is_top(i) else b(parent_idx)
        return floor2(parent - 1)

    top = t(k)
    bottom = b(k)
    return '{} {}'.format(int(top), int(bottom))

T = int(raw_input())
for i in xrange(T):
    n, k = raw_input().split()
    print('Case #{}: {}'.format(i + 1, f(int(n), int(k))))
