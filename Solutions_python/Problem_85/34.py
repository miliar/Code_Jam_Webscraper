from itertools import cycle

def parse(f):
    rows = [r.strip().split(' ') for r in open(f).read().split('\n') if r]
    num_tests = rows.pop(0)
    case = 1
    for row in rows:
        solve(int(row[0]), int(row[1]), int(row[2]), map(int,row[4:]), case)
        case += 1

def solve(L,t,N,C,case):
    c = cycle(C)
    distances = [c.next() for i in xrange(N)]
    remaining = int(t*0.5)
    the_total = sum(d*2 for d in distances)
    if L > 0 or t < the_total:
        for i in xrange(len(distances)):
            distances[i] -= remaining
            if distances[i] >= 0:
                break
            else:
                remaining = -distances[i]
                distances[i] = 0
        distances = sorted([d for d in distances if d > 0], reverse=True)
        total = t
        total += sum(d for d in distances[:L])
        total += sum([d*2 for d in distances[L:]])
    else:
        total = the_total
    print 'Case #%d: %d' % (case, total)


f = 'B-large.in'
parse(f)
