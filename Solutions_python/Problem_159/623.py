import sys
from math import ceil


def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        for i in range(nr_cases):
            fp.readline()
            m = map(int, fp.readline().split())
            cases.append(m)
    return cases


def m1(case):
    total = 0
    for i, v in enumerate(case[1:]):
        if case[i] - v > 0:
            total += (case[i] - v)
    return total


def m2(case):
    min_rate = 0
    for i, v in enumerate(case[1:]):
        diff = case[i] - v
        if diff > 0:
            min_rate = max(min_rate, (case[i] - v))
    total = 0
    for i, v in enumerate(case[1:]):
        diff = v - case[i]
        print i, case[i], v, diff

        if case[i] > 0:
            # she can eat
            if case[i] >= min_rate:
                total += min_rate
            else:
                if v >= case[i]:
                    total += case[i]
                else:
                    total += min(min_rate, case[i])
    return total


def solve(cases):
    output = ''
    print cases
    for i, c in enumerate(cases):
        m1_res = m1(c)
        m2_res = m2(c)
        output += 'Case #%d: %d %d\n' % (i+1, m1_res, m2_res)
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)
    output = solve(cases)

    with open(out, 'w') as fp:
        fp.write(output)
