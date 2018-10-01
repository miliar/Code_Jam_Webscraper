
def mul(a, b):
    if a < 0:
        return -mul(-a, b)
    if b < 0:
        return -mul(a, -b)
    if a == 1 or b == 1:
        return a * b
    if a == b:
        return -1
    return quat[(a, b)]

quat = {
    (2, 3): 4,
    (3, 2): -4,
    (3, 4): 2,
    (4, 3): -2,
    (4, 2): 3,
    (2, 4): -3,
}


def find_i(arr):
    prod = 1
    for i, x in enumerate(arr):
        prod = mul(prod, x)
        if prod == 2:
            return (True, i + 1)
    return False, -1


def find_k(arr):
    prod = 1
    for i, x in enumerate(reversed(arr)):
        prod = mul(x, prod)
        if prod == 4:
            return (True, i + 1)
    return False, -1


def ok(arr, X):
    found_i, len_i = find_i(arr * min(10, X))
    found_k, len_k = find_k(arr * min(10, X))
    # print found_i, len_i, found_k, len_k
    return found_i and found_k and len_i + len_k < len(arr) * X

T = int(raw_input())

for z in range(T):
    L, X = map(int, raw_input().split())
    arr = map(lambda x: 2 if x == 'i' else 3 if x == 'j' else 4, raw_input())
    # print L, X, arr
    prod = 1
    for x in arr:
        prod = mul(prod, x)
    print 'Case #{}: '.format(z + 1),
    if prod == 1:
        print 'NO'
    elif prod == -1:
        print 'YES' if X % 2 == 1 and ok(arr, X) else 'NO'
    else:
        print 'YES' if X % 4 == 2 and ok(arr, X) else 'NO'

# print 1, 1, mul(1, 1)
# print 1, 2, mul(1, 2)
# print 1, 3, mul(1, 3)
# print 1, 4, mul(1, 4)
# print 1, -1, mul(1, -1)
# print 1, -2, mul(1, -2)
# print 1, -3, mul(1, -3)
# print 1, -4, mul(1, -4)

# print -1, 1, mul(-1, 1)
# print -1, 2, mul(-1, 2)
# print -1, 3, mul(-1, 3)
# print -1, 4, mul(-1, 4)
# print -1, -1, mul(-1, -1)
# print -1, -2, mul(-1, -2)
# print -1, -3, mul(-1, -3)
# print -1, -4, mul(-1, -4)

# print 2, 1, mul(2, 1)
# print 2, 2, mul(2, 2)
# print 2, 3, mul(2, 3)
# print 2, 4, mul(2, 4)
# print 2, -1, mul(2, -1)
# print 2, -2, mul(2, -2)
# print 2, -3, mul(2, -3)
# print 2, -4, mul(2, -4)

# print -2, 1, mul(-2, 1)
# print -2, 2, mul(-2, 2)
# print -2, 3, mul(-2, 3)
# print -2, 4, mul(-2, 4)
# print -2, -1, mul(-2, -1)
# print -2, -2, mul(-2, -2)
# print -2, -3, mul(-2, -3)
# print -2, -4, mul(-2, -4)

# print 3, 1, mul(3, 1)
# print 3, 2, mul(3, 2)
# print 3, 3, mul(3, 3)
# print 3, 4, mul(3, 4)
# print 3, -1, mul(3, -1)
# print 3, -2, mul(3, -2)
# print 3, -3, mul(3, -3)
# print 3, -4, mul(3, -4)

# print -3, 1, mul(-3, 1)
# print -3, 2, mul(-3, 2)
# print -3, 3, mul(-3, 3)
# print -3, 4, mul(-3, 4)
# print -3, -1, mul(-3, -1)
# print -3, -2, mul(-3, -2)
# print -3, -3, mul(-3, -3)
# print -3, -4, mul(-3, -4)

# print 4, 1, mul(4, 1)
# print 4, 2, mul(4, 2)
# print 4, 3, mul(4, 3)
# print 4, 4, mul(4, 4)
# print 4, -1, mul(4, -1)
# print 4, -2, mul(4, -2)
# print 4, -3, mul(4, -3)
# print 4, -4, mul(4, -4)

# print -4, 1, mul(-4, 1)
# print -4, 2, mul(-4, 2)
# print -4, 3, mul(-4, 3)
# print -4, 4, mul(-4, 4)
# print -4, -1, mul(-4, -1)
# print -4, -2, mul(-4, -2)
# print -4, -3, mul(-4, -3)
# print -4, -4, mul(-4, -4)
