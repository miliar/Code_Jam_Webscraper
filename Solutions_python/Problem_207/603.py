from collections import namedtuple, Counter

Test = namedtuple('Test', 'counts')

def read(line):
    return Test(Counter(dict(zip('ROYGBV', map(int, line.split()[1:])))))

def solve(test):
    colors = {'R', 'Y', 'B'}
    maj = max(colors, key=test.counts.get)
    if test.counts[maj] > sum(test.counts.values()) / 2:
        return 'IMPOSSIBLE'

    counts = Counter(test.counts)
    stalls = ''
    while counts:
        cols = colors - ({stalls[-1]} if stalls else set())
        maxc = max(cols, key=lambda k: (counts.get(k, 0), k == maj))
        stalls += maxc
        counts[maxc] -= 1
        counts = Counter({k: v for k, v in counts.items() if v > 0})
    return stalls

if __name__ == '__main__':
    infile = 'B-small-attempt2.in'

    with open(infile) as src:
        lines = list(src.readlines())

    number = int(lines[0])
    tests = [read(line) for line in lines[1:]]

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
