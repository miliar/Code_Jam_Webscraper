# !/usr/bin/python

# By Jesse -- jesse.wanderer@gmail.com

def get_item(n):
    ls = []
    for i in range(n):
        ls.append(raw_input())
    return ls

def main():
    S = int(raw_input())
    engines = get_item(S)
    Q = int(raw_input())
    if Q == 0:
        print 0
        return
    queries = get_item(Q)

    ix = 0
    switch = 0
    while ix < Q:
        ix += find_last(engines, queries[ix:])
        switch += 1
    print switch - 1

def find_last(engines, queries):
    eng_set = set(engines)
    que_set = set(queries)
    if len(eng_set) > len(que_set):
        return len(queries)
    elif len(eng_set) < len(que_set):
        print 'error:some query is not engine name!'
        return len(queries)

    appeared = set([])
    last = -1
    for i in range(len(queries)):
        if queries[i] not in appeared and i > last:
            last = i
            appeared.add(queries[i])
    return last

n = int(raw_input())
for i in xrange(n):
    print 'Case #%d:' % (i+1),
    main()
