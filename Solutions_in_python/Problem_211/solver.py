from collections import namedtuple
from functools import reduce
from operator import mul
from itertools import combinations as C

Test = namedtuple('Test', 'N K U cores')

def read(lines):
    while lines:
        N, K = map(int, lines[0].split())
        U = float(lines[1])
        cores = tuple(sorted(map(float, lines[2].split())))
        yield Test(N, K, U, cores)
        lines = lines[3:]

def solve(test):
    def arrange(cores):
        for n in range(len(cores), 0, -1):
            average = (test.U + sum(cores[:n])) / n
            if all(average >= p for p in cores[:n]):
                cores = [average] * n + cores[n:]
                break
        print(test.cores)
        print(test.U)
        print(cores)

        return cores

    cores = list(test.cores)
    cores[-test.K:] = arrange(cores[-test.K:])
    if test.N == test.K:
        return reduce(mul, cores)
    else:
        combs = C(cores, test.K)
        return 1 - reduce(mul, (reduce(mul, (1 - s for s in cs)) for cs in combs))

if __name__ == '__main__':
    infile = 'C-small-1-attempt1.in'

    with open(infile) as src:
        lines = list(src.readlines())

    number = int(lines[0])
    tests = list(read(lines[1:]))

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            print(i)
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
