# -*- coding: utf-8 -*-
            
remember = {}

def hash_list(cur, l):
    str = ""
    for e in l:
        str += e
    return cur+str

def solve(current, engines, reqs):
    hash = hash_list(current, reqs)
    try:
        return remember[hash]
    except KeyError:
        pass

    if not reqs:
        remember[hash] = 0
        return 0
    #print current, engines, reqs

    if current == reqs[0]:
        min = 9999
        for e in engines:
            if e == current:
                continue
            c = solve(e, engines, reqs[1:])
            if c < min:
                min = c
        min = min + 1
    else:
        min = solve(current, engines, reqs[1:])
    remember[hash] = min
    return min

f = open('input', 'r')
lines = f.readlines()
n = int(lines[0])
i = 1
for testcase in range(n):
    search_engine_n = int(lines[i])
    i += 1
    engines = lines[i:i+search_engine_n]
    i += search_engine_n
    req_n = int(lines[i])
    i += 1

    reqs = lines[i:i+req_n]
    i += req_n

    min = 9999
    for e in engines:
        if reqs and e == reqs[0]:
            continue
        c = solve(e, engines, reqs)
        if c < min:
            min = c
    print 'Case #%s: %s' % (testcase + 1, min)
