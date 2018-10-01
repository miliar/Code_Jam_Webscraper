T = int(raw_input())


def quaternions(x, y):
    if x == y == '1':
        return '1'
    elif x == y:
        return '-1'
    elif x == '1':
        return y
    elif y == '1':
        return x
    elif x == 'i' and y == 'j':
        return 'k'
    elif x == 'i' and y == 'k':
        return '-j'
    elif x == 'j' and y == 'i':
        return '-k'
    elif x == 'j' and y == 'k':
        return 'i'
    elif x == 'k' and y == 'i':
        return 'j'
    elif x == 'k' and y == 'j':
        return '-i'


def multiply(x, y):
    if x[:1] == '-' and y[:1] == '-':
        result = '%s' % quaternions(x[1:2], y[1:2])
    elif x[:1] == '-':
        result = '-%s' % quaternions(x[1:2], y)
    elif y[:1] == '-':
        result = '-%s' % quaternions(x, y[1:2])
    else:
        result = quaternions(x, y)

    return result[2:] if result[:1] == result[1:2] == '-' else result


def search(c, s, start=0, last_char=False):
    c_found = False
    start_idx = start
    end_idx = start + 2
    cache = None
    while not c_found:
        chunk = s[start_idx:end_idx]
        r = multiply(cache, chunk) if cache else multiply(chunk[:1], chunk[1:2])
        cache = r

        if last_char:
            c_found = r == c and end_idx == len(s)
        else:
            c_found = r == c

        if c_found:
            break
        elif last_char and end_idx == len(s):
            break
        elif not last_char and end_idx == len(s) - 2:
            break
        else:
            end_idx += 1
            start_idx = end_idx - 1
    return c_found, end_idx

for case in range(T):
    L, X = map(lambda x: int(x), raw_input().split())
    chars = raw_input()

    if L == 1 or L * X < 3:
        solution = 0
    elif L * X == 3:
        solution = (chars * X == 'ijk')
    else:
        s = chars * X

        i_found, idx = (True, 1) if s[:1] == 'i' else search('i', s)
        j_found, idx = search('j', s, idx) if i_found else (False, idx)
        k_found, idx = search('k', s, idx, last_char=True) if j_found else (False, idx)

        solution = 1 if all([i_found, j_found, k_found]) else 0

    print 'Case #%d: %s' % (case+1, 'YES' if solution == 1 else 'NO')