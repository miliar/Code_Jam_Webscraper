import itertools

f = open('C-small-attempt0.in')
f_out = open('ProbC-large.out', 'w')
n = int(f.next())
test = 1

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield [i for i in indices]
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield indices

def any_nonzero(c_list):
    for c in c_list:
        if c != 0: return True

def fail_sum(c_list):
    res = 0
    for c in c_list:
        res ^= c
    return res


while test <= n:
    _ = int(f.next())
    values = [int(x) for x in f.next().split(' ')]
    values.sort()
    sean_sum = 0
    pat_sum = 0
    max_sum = -1
    for i in xrange(len(values)-1):
        combs = combinations(values, len(values)-i-1)
        for c in combs:
            pats = [x for x in range(len(values)) if x not in c]
            sean_c = [values[x] for x in c]
            pats_c = [values[x] for x in pats]
            sean_sum = sum(sean_c)
            if sean_sum > max_sum:
                pats_sum = sum(pats_c)
                if sean_sum >= pats_sum:
                    sean_fs = fail_sum(sean_c)
                    pats_fs = fail_sum(pats_c)
                    if sean_fs == pats_fs:
                        max_sum = sean_sum
    if max_sum != -1:
        f_out.write('Case #%d: %d\n' %(test, max_sum))
    else:
        f_out.write('Case #%d: NO\n' %(test,))
    test += 1
