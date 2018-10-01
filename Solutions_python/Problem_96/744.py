"""Dancing with the Googlers"""

import sys



def split_total_points(total):
    """returns {'not surprising': (a, b, c), 'surprising': (a', b', c')},
    where (a,b,c) is a triplet of scores with the highest best result.
    Similar for (a', b', c'), in a surprising result.
    """
    not_surprising = None
    surprising = None
    base = total // 3
    rest = (total - base*3)
    assert rest == total % 3

    if rest == 0:
        not_surprising = (base, base, base)
        if 0 < base < 10:
            surprising = (base-1, base, base+1)
        else:
            surprising = (base, base, base)
    elif rest == 1:
        not_surprising = (base, base, base+1)
        surprising = (base, base, base+1)
    elif rest == 2:
        not_surprising = (base, base+1, base+1)
        if base < 9:
            surprising = (base, base, base+2)
        else:
            surprising = (base, base+1, base+1)
    else:
        assert False, "rest > 2 ??"
    assert len([b for b in surprising+not_surprising if b > 10 or b < 0]) == 0, (surprising, not_surprising, total)
    assert sum(not_surprising) == sum(surprising) == total
    assert max(not_surprising) - min(not_surprising) <= 2, (total, base, not_surprising)
    assert max(surprising) - min(surprising) <= 2, (total, base, surprising)

    return {'not surprising': not_surprising,
            'surprising': surprising}

def decide(input):
    parts = [int(i) for i in input.split()]
    n_googlers, n_surprising, p = parts[:3]
    points = parts[3:]
    ge_p = []
    results = []
    for total in points:
        results.append(split_total_points(total))

    def sort_key(item):
        max_not = max(item['not surprising'])
        if max_not >= p:
            return max_not
        return max(item['surprising'])
    results.sort(key=sort_key, reverse=True)
    for r in results:
        if max(r['not surprising']) >= p:
            ge_p.append(r)
        elif n_surprising > 0 and max(r['surprising']) >= p:
            ge_p.append(r)
            n_surprising -= 1
    return len(ge_p)

def run(infile):
    f = open(infile)
    num = int(f.readline())
    for i in xrange(num):
        line = f.readline().strip()
        print 'Case #{count}: {}'.format(decide(line), count=i+1)


if __name__ == '__main__':
    run(sys.argv[1])
