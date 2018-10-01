#!/usr/bin/python

from collections import defaultdict

BASE_ELEMENTS = set([str(x) for x in 'QWERASDF'])

for case in range(input()):
    data = raw_input().split()
    C = int(data[0])
    combine = dict()
    for comb in [str(x) for x in data[1:1 + C]]:
        first, second, result = comb
        combine[first + second] = result
        combine[second + first] = result
    D = int(data[1 + C])
    opposed = defaultdict(list)
    for op in [str(x) for x in data[2 + C:2 + C + D]]:
        opposed[op[0]].append(op[1])
        opposed[op[1]].append(op[0])
    N = int(data[1 + C + 1 + D])
    elements = str(data[-1])
    out = []
    count = defaultdict(int)
    for e in elements:
        out.append(e)
        count[e] = count[e] + 1
        if len(out) < 2:
            continue
        pair = out[-1] + out[-2]
        if pair in combine:
            count[pair[0]] = count[pair[0]] - 1
            count[pair[1]] = count[pair[1]] - 1
            out.pop()
            out[-1] = combine[pair]
        last = out[-1]
        opp = set(opposed[last])
        for b in BASE_ELEMENTS:
            if count[b] > 0 and b in opp:
                out = []
                count.clear()

    print "Case #%s: [%s]" % (case + 1, ', '.join(out))
