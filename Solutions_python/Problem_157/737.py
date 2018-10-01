from collections import namedtuple

T = int(raw_input())

_, one, i, j, k = range(5)

MUL_CACHE = {
    (one, one): one,
    (one, i): i,
    (one, j): j,
    (one, k): k,

    (i, one): i,
    (i, i): -one,
    (i, j): k,
    (i, k): -j,

    (j, one): j,
    (j, i): -k,
    (j, j): -one,
    (j, k): i,

    (k, one): k,
    (k, i): j,
    (k, j): -i,
    (k, k): -one,
}

def multiply(a, b):
    sign = True
    if a < 0:
        a *= -1
        sign = not sign
    if b < 0:
        b *= -1
        sign = not sign

    assert a in (one, i, j, k)
    assert b in (one, i, j, k)

    ret = MUL_CACHE[(a, b)]

    if sign:
        return ret
    return -ret

def reduce_quarternion_mul(s, debug=False):
    ret = one
    for letter in s:
        if debug:
            print 'multiplying in {}'.format(letter)
        value = {'i': i, 'j': j, 'k': k}[letter]
        assert value in (i, j, k)
        ret = multiply(ret, value)
        if debug:
            print 'got {}'.format(ret)
    return ret

def chunk(s, target):
    if s == None:
        return None, None

    value = one
    for count in range(len(s)):
        letter = {'i': i, 'j': j, 'k': k}[s[count]]
        assert letter in (i, j, k)
        value = multiply(value, letter)
        if value == target:
            return s[:count+1], s[count+1:]

    return None, None


for case in range(T):
    answer = "NO"

    L, X = map(int, raw_input().split())
    s = raw_input() * X

    a, s = chunk(s, i)
    b, s = chunk(s, j)
    c = s
    if c is not None and reduce_quarternion_mul(c) == k:
        answer = "YES"

    print "Case #{}: {}".format(case + 1, answer)
