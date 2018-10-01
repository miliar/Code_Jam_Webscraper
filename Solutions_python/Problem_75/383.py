from collections import defaultdict
def case():
    line = raw_input().split()
    C = int(line[0])
    combine = dict((comb[:2], comb[2]) for comb in line[1:1+C])
    for k, v in combine.items():
        combine[k[::-1]] = v
    D = int(line[1+C])
    oppose = line[2+C:2+C+D]
    oppose += [op[::-1] for op in oppose]
    oppose = set(oppose)
    invoke = line[-1]
    base = "QWERASDF"

    """
    print ' '.join(line)
    print combine
    print oppose
    assert int(line[-2]) == len(invoke)
    """

    s = defaultdict(int)
    l = []
    for el in invoke:
        l.append(el)
        if len(l) >= 2 and l[-2] + l[-1] in combine:
            s[l[-2]] -= 1
            l[-2:] = [combine[l[-2] + l[-1]]]
        else:
            for b in base:
                if s[b] > 0 and (b+el in oppose or el+b in oppose):
                    s = defaultdict(int)
                    l = []
                    break
            else:
                s[el] += 1
#        print l
    return l

T = int(raw_input())
for i in xrange(1, T+1):
    print 'Case #%i: [%s]' % (i, ', '.join(case()))
