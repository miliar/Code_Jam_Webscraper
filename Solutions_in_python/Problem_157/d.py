pos = {1: 0, 'i': 1, 'j': 2, 'k': 3}
maps = [
    [1, 'i', 'j', 'k'],
    ['i', -1, 'k', '-j'],
    ['j', '-k', -1, 'i'],
    ['k', 'j', '-i', -1]
]

def get_op(a):
    if a in [1, 'i', 'j', 'k']:
        return 1, a
    elif a in [-1, '-i', '-j', '-k']:
        if a == -1:
            return -1, 1
        else:
            return -1, a[1]
    else:
        print 'Unknown op: ', a
        raise


def cal(ao, av, bv):
    # ao, av = get_op(a)
    co, cv = get_op(maps[pos[av]][pos[bv]])
    return ao*co, cv


def get_range(l, s, start, end):
    o, v = 1, 1
    for i in xrange(start, end):
        o, v = cal(o, v, s[i%l])
    return o, v


def work(l, x, s):
    # print l, x, s,
    if l == 1:
        return 'NO'
    o, v = get_range(l, s, 0, l * x)
    # print 'o, v:', o, v
    if o != -1 or v != 1:
        return 'NO'
    i_o, i_v = 1, 1
    for i in xrange(0, l * x):
        i_o, i_v = cal(i_o, i_v, s[i%l])
        if i_o == 1 and i_v == 'i':
            j_o, j_v = 1, 1
            for j in xrange(i+1, l * x):
                j_o, j_v = cal(j_o, j_v, s[j%l])
                if j_o == 1 and j_v == 'j':
                    k_o, k_v = 1, 1
                    for k in xrange(j+1, l * x):
                        k_o, k_v = cal(k_o, k_v, s[k%l])
                    if k_o == 1 and k_v == 'k':
                        return 'YES'
    return 'NO'


if __name__ == '__main__':
    import fileinput
    f = fileinput.input()

    t = int(f.readline())
    for ti in range(1, t+1):
        l, x = [int(x) for x in f.readline().split()]
        s = f.readline()
        ans = work(l, x, s)
        print 'Case #%d: %s' % (ti, ans)