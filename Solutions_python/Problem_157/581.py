def quat(a, b):
    if a == '1':
        return b, True
    elif a == b:
        return '1', False
    elif a == 'i':
        if b == 'j': return 'k', True
        else: return 'j', False
    elif a == 'j':
        if b == 'i': return 'k', False
        else: return 'i', True
    elif a == 'k':
        if b == 'i': return 'j', True
        else: return 'i', False

def solve():
    L, X = (int(i) for i in raw_input().split())
    s = raw_input()
    s = s*X


    i = 0
    a = '1'
    sign = True

    while i < L * X and a != 'i':
        a, next_sign = quat(a, s[i])
        sign = (sign == next_sign)
        i += 1
    if a != 'i': return False

    a = '1'
    while i < L * X and a != 'j':
        a, next_sign = quat(a, s[i])
        sign = (sign == next_sign)
        i += 1
    if a != 'j': return False

    a = '1'
    while i < L * X:
        a, next_sign = quat(a, s[i])
        sign = (sign == next_sign)
        i += 1
    if a != 'k' or not sign: return False

    return True

def main():
    N = int(raw_input())
    for i in xrange(N):
        print "Case #{0}: {1}".format(i + 1, 'YES' if solve() else 'NO')


if __name__ == '__main__':
    main()
