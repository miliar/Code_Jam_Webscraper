import sys


def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        for i in range(nr_cases):
            data = fp.readline().split()
            smax = int(data[0])
            audience = []
            for j in data[1]:
                audience.append(int(j))
            case = (smax, audience)
            cases.append(case)
    return cases


def solve(cases):
    output = ''
    for i, c in enumerate(cases):
        standing = 0
        added = 0
        for j, a in enumerate(c[1]):
            if standing + added < j:
                added += (j - standing - added)
            standing += a
        output += "Case #%d: %d\n" % (i+1, added)
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)
    output = solve(cases)

    with open(out, 'w') as fp:
        fp.write(output)
