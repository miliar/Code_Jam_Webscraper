import bisect
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
def gen():
    yield 0
    l = 1
    x = 0
    while x < 18:
        for i in combinations_with_replacement('123456789', l):
            yield int(''.join(i))
        l += 1
        x+=1
p = gen()
a = []
for i in p : a.append(i)
f = open('input.in')
t = int(f.readline().strip())
for i in range(1,t+1):
    ip = int(f.readline())
    index = bisect.bisect(a, ip)
    print 'Case #' + str(i) + ': ' + str(a[index-1])