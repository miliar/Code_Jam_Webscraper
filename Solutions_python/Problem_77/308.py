import random

def components(numbers):
    opts = list(numbers)
    results = []
    while len(opts) > 0:
        component = []
        p = opts[0]
        while True:
            if p in component or len(opts) == 0:
                break
            component.append(p)
            opts.remove(p)
            p = numbers.index(p)
        results.append(len(component))
    return results

cache = {0:0,1:0,2:2}

def init():
    for i in xrange(10):
        n = i + 3
        cache[n] = compute(n)

def compute(n):
    s = 0
    m = 100000
    for k in xrange(m):
        numbers = []
        for j in xrange(n):
            numbers.append((j + 1) % n)
        s = s + pre_sort(numbers)
    return s * 1.0 / m

def pre_compute(m):
    for i in xrange(m):
        if not cache.has_key(i+1):
            cache[i+1] = compute(i+1)

def cache_or_compute(n):
    if cache.has_key(n):
        return cache[n]
    else:
        pre_compute(n)
    return cache[n]

def pre_sort(numbers):
    s = 0
    while True:
        s = s + 1
        random.shuffle(numbers)
        coms = components(numbers)
        if len(coms) == 1:
            continue
        for c in coms:
            s = s + cache[c]
        break
    return s

def after_sort(numbers):
    s = 0
    coms = components(numbers)
    for c in coms:
        s = s + cache_or_compute(c)
    return s

def sort(line):
    parts = line.strip().split(' ')
    numbers = [int(k)-1 for k in parts]
    return after_sort(list(numbers))

with open('D-small-attempt1.in', 'r') as f:
    line = f.readline()
    t = int(line)
    #init()
    for i in range(t):
        line = f.readline()
        line = f.readline()
        m = sort(line)
        print 'Case #%d: %.6f' % (i + 1, round(m))
