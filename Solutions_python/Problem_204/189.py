#!/usr/bin/env python3

from collections import defaultdict
from operator import itemgetter
import math

import sys
sys.setrecursionlimit(1000000)

class Edge:
    def __init__(self, u, v, cap):
        self.source = u
        self.target = v
        self.capacity = cap


class FlowSolver:
    def __init__(self):
        self.adj = defaultdict(list)
        self.flow = defaultdict(int)

    def append(self, u, v, cap):
        go = Edge(u, v, cap)
        self.adj[u].append(go)

        back = Edge(v, u, 0)  # XXX
        self.adj[v].append(back)

    def find_path(self, u, v):
        def iter(u, v, path, visited):
            if u == v:
                return path

            if u in visited:
                assert False
                return []
            visited.add(u)

            for c in self.adj[u]:
                if c.target in visited:
                    continue

                residue = c.capacity - self.flow[(u, c.target)] + self.flow[(c.target, u)]
                if residue <= 0:
                    continue

                ret = iter(c.target, v, path + [((u, c.target), residue)], visited)
                if ret:
                    return ret
            return []

        return iter(u, v, [], set())


    def solve(self, u, v):
        while True:
            path = self.find_path(u, v)
            if not path:
                break
            delta = min(map(itemgetter(1), path))

            for (f, t), _ in path:
                flow = self.flow[(f, t)] - self.flow[(t, f)] + delta
                self.flow[(f, t)] = max(0, flow)
                self.flow[(t, f)] = max(0, -flow)


def solve(N, P, recipe, packages):
    solver = FlowSolver()

    if len(recipe) > 0:
        i = 0
        for j in range(P):
            solver.append('source', ('TI', i, j), 1)

    legacy = defaultdict(list)
    for i in range(N):
        need = recipe[i]
        ps = packages[i]

        sprout = defaultdict(list)
        chains = set()
        for j, have in enumerate(ps):
            lb = max(1, math.ceil(have / need / 1.1))  # we should make at least 1 serving to make it right
            ub = math.floor(have / need / 0.9)
            if not lb <= ub:
                continue

            for x in range(lb, ub+1):
                for l_node in legacy[x]:
                    tag, a, b = l_node
                    assert(tag == 'TO')
                    chains.add(('L_TI', a, b, i, j))

            solver.append(('TI', i, j), ('TO', i, j), 1)  # limit the package use to 1.

            for x in range(lb, ub+1):
                sprout[x].append(('TO', i, j))

        for chain in chains:
            tag, a, b, i, j = chain
            assert(tag == 'L_TI')
            l_node = ('TO', a, b)
            solver.append(l_node, ('TI', i, j), 1)
        legacy = sprout


    if len(recipe) > 0:
        i = N - 1
        for j in range(P):
            solver.append(('TO', i, j), 'sink', 1)

    solver.solve('source', 'sink')

    source_flow = 0
    sink_flow = 0
    for (f, t), v in solver.flow.items():
        if f == 'source':
            source_flow += v
        if t == 'sink':
            sink_flow += v

    assert(source_flow == sink_flow)
    return sink_flow


T = int(input())

for case_number in range(1, T+1):
    N, P = map(int, input().split())
    recipe = [int(x) for x in input().split()]
    packages = []

    for n in range(N):
        ps = [int(x) for x in input().split()]
        assert len(ps) == P
        packages.append(ps)

    print('Case #%d:' % case_number, solve(N, P, recipe, packages))
