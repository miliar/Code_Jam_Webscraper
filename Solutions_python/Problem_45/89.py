#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""

def permut(items, n):
    if n==0: 
        yield []
    else:
        for i in xrange(len(items)):
            for cc in permut(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def main():
    for casenum in range(input()):
        n_cells, n_releasers = [int(i) for i in raw_input().split()]
        cells = [int(i)-1 for i in raw_input().split()]

        all_var = list(permut(cells, len(cells)))
        all_count = len(all_var)
        total = []

        for perm in all_var:
            prison = [1 for i in range(n_cells)]
            coins = 0

            for var in perm:
                prison[var] = 0
                if var < n_cells - 1:
                    for v in range(var + 1, n_cells):
                        if prison[v] == 0:
                            break
                        coins += 1
                if var > 0:
                    for v in range(var - 1, -1, -1):
                        if prison[v] == 0:
                            break
                        coins += 1

            total.append(coins)    

        print 'Case #%d: %d' % (casenum + 1, min(total))

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    main()
