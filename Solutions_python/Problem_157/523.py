"""
This script may use libraries publicly available at: https://github.com/grokit/dcore.

Does this solution solve:
   Small: ?.
   Big:   ?.
"""

import dcore.gcj_boot as boot

dijkD = {}
dijkD['1'] = {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'}
dijkD['i'] = {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'}
dijkD['j'] = {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'}
dijkD['k'] = {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}

def dijkFn(a, b):
    ##print('disjkFn a',a,'b', b)
    neg = 0
    if len(a) == 2:
        assert a[0] == '-'
        a = a[1]
        neg += 1

    if len(b) == 2:
        assert b[0] == '-'
        b = b[1]
        neg += 1

    if neg == 1:
        pre = '-'
    else:
        pre = ''

    rv = pre + dijkD[a][b]

    # fix double neg
    if len(rv) == 3:
        assert rv[0] == '-'
        assert rv[1] == '-'
        rv = rv[2]

    return rv

def readProblem(fh):
    l, x = [int(x) for x in fh.readline().strip().split()]
    chars = fh.readline().strip()
    chars = [c for c in chars]
    return (l, x, chars)

def reduceD(a):
    ##print('reduce', a)
    if len(a) == 0:
        return a

    c = a[0]
    for i in range(1, len(a)):
        c = dijkFn(c, a[i])
    return c

def solve(p):
    toEAT = {'None': 'i', 'i': 'j', 'j':'k'}

    l, x, chars = p
    if len(chars) == 0:
        return False

    # replace by set of hashable State
    graph = {'1': set()}
    graph['1'].add('None')
    # None: did not accumulate anything
    # i: accumulated a i, looking for a j
    # [...]
    # k: accumulated i,j,k HAVE TO EAT EVERYTHING and keep changind state.

    sGraph = ''
    mem = {}

    i = 0
    jj = 0
    while i < x:

        sgi = str(graph)

        if sgi in mem:
            graph, iLast = mem[sgi] 
            #print("i, iLast", i, iLast)
            #print("i- iLast", i- iLast)
            period = i-iLast
            iterLeft = (x-i-1) % period
            i = x - iterLeft
            continue
        else:
            for c in chars:
                jj +=1
                newG = {}

                # k: letter of curr state in graph
                for k, lset in graph.items():
                    for acc in lset:

                        # case 1: we multiply the letter and change state
                        newState = reduceD([k] + [c])
                        if newState not in newG:
                            newG[newState] = set()
                        newG[newState].add(acc)

                        # case 2: we 'eat' that letter and return to state 1
                        if acc in toEAT and newState == toEAT[acc]:
                            acc = toEAT[acc]
                            newState = '1'
                            if newState not in newG:
                                newG[newState] = set()
                            newG[newState].add(acc)

                graph = newG

        mem[sgi] = graph, i 
        i += 1


    #print('total num it', jj)
    # win: acc = k in states k and 1
    if '1' in graph:
        for acc in graph['1']:
            if acc == 'k':
                return 'YES'
    return 'NO'

boot.solve(solve, readProblem, '.*large')
