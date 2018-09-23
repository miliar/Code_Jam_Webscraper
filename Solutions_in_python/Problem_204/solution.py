import argparse
import itertools
import multiprocessing
import sys
import time
from fractions import Fraction


def global_solve(index):
    """A dirty way to get around pickling limitations when multiprocessing."""
    return global_solve.instance.solve_single(index)


class Problem(object):
    """
    A simple helper class for parsing Google Code Jam problem inputs and
    formatting solutions.

    It also allows paralellizing tasks by multiprocessing in order to work
    around Python's limited (due to GIL) threading.

    (C) Vytautas Liuolia 2016-2017
    """

    SAMPLE = None

    def __init__(self):
        self.cases = []

    def parse_case(self, lines):
        raise NotImplementedError

    def solve(self, case):
        raise NotImplementedError

    def solve_single(self, index):
        start = time.time()
        result = str(self.solve(self.cases[index]))
        elapsed = time.time() - start
        return result, elapsed

    def read_cases(self, lines=None):
        if lines is None:
            lines = (line.strip() for line in sys.stdin)
        amount = int(lines.next())
        for index in xrange(amount):
            self.cases.append(self.parse_case(lines))

    def solve_all(self, processes=None, verbose=False):

        indices = xrange(len(self.cases))
        processes = processes or multiprocessing.cpu_count()

        if processes > 1:
            global_solve.instance = self
            pool = multiprocessing.Pool(processes=processes)
            results = pool.imap(global_solve, indices)
        else:
            results = itertools.imap(self.solve_single, indices)

        for index, (result, elapsed) in enumerate(results):
            if verbose:
                message = "Solved case #{0} in {1} s\n".format(
                    index + 1, round(elapsed, 6))
                sys.stderr.write(message)
                sys.stderr.flush()
            print "Case #{0}: {1}".format(index + 1, result)
            sys.stdout.flush()

    @classmethod
    def main(cls):
        parser = argparse.ArgumentParser(
            description='Reads Code Jam problem input and outputs solutions.')
        parser.add_argument(
            '-s', '--sample', action='store_true',
            help='run the predefined sample instead of input')
        parser.add_argument(
            '-v', '--verbose', action='store_true',
            help='print progress information in stderr')
        parser.add_argument(
            '-p', '--processes', type=int, default=0,
            help='amount of processes to use (default: CPU count)')
        args = parser.parse_args()

        lines = None
        if args.sample:
            if cls.SAMPLE is None:
                raise NotImplementedError
            lines = iter(cls.SAMPLE.splitlines())

        problem = cls()
        problem.read_cases(lines)
        problem.solve_all(processes=args.processes, verbose=args.verbose)


INF = sys.maxsize


def hopcroft_carp(U):

    def bfs():
        queue = set()
        dist[None] = INF

        for u in U:
            if pair_u[u] is None:
                dist[u] = 0
                queue.add(u)
            else:
                dist[u] = INF

        while queue:
            u = queue.pop()
            if dist[u] < dist[None]:
                for v in U[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.add(pair_v[v])

        return dist[None] != INF

    def dfs(u):
        if u is not None:
            for v in U[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    dist = {}
    pair_u = {}
    pair_v = {}
    for u, adj in U.iteritems():
        pair_u[u] = None
        pair_v.update((v, None) for v in adj)

    while bfs():
        for u in U:
            if pair_u[u] is None:
                dfs(u)

    return {u: v for u, v in pair_u.iteritems() if v is not None}


class Package(object):

    def __init__(self, r, amount):
        self.amount = amount
        h = amount*10/9/r
        l = amount*10/11/r
        if amount*10 % (11*r) != 0:
            l += 1
        self.range = (l, h)

    def __repr__(self):
        return "Package<{} {}>".format(self.amount, tuple(self.range))

    def __nonzero__(self):
        l, h = self.range
        return l <= h

    def overlaps(self, other):
        l, h = self.range
        lo, lh = other.range
        return not ((h < lo) or (lh < l))


class Solution(Problem):

    SAMPLE_LARGE = """6
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900
"""
    SAMPLE = """5
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
"""

    def solve(self, case):
        N, P, R, packages = case
        assert 1 <= N <= 2  # Small dataset

        first = filter(None, [Package(R[0], p) for p in packages[0]])
        if N == 1:
            return len(first)

        second = filter(None, [Package(R[1], p) for p in packages[1]])

        graph = {}
        for package in first:
            graph[package] = [p for p in second if package.overlaps(p)]

        matching = hopcroft_carp(graph)
        # print graph
        # print matching
        return len(matching)

    def parse_case(self, lines):
        N, P = map(int, lines.next().split())
        R = map(int, lines.next().split())
        packages = [map(int, lines.next().split()) for n in xrange(N)]
        return N, P, R, packages


if __name__ == '__main__':
    Solution.main()
