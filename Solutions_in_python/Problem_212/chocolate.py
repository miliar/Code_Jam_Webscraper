

from solution import Solution


class Case(object):
    def __init__(self, n, p, gs):
        self.n = n
        self.p = p
        self.gs = gs

    def small_solve(self):
        mods = [g % self.p for g in self.gs]
        if self.p == 2:
            t = mods.count(0)
            d = mods.count(1)
            r = bool(d % 2)
            return t + d/2 + r
        if self.p == 3:
            a = mods.count(1)
            b = mods.count(2)
            d = abs(a-b)
            total = mods.count(0) + min(a, b)
            r = bool(d % 3)
            return total + d/3 + r
        if self.p == 4:
            t = mods.count(0)
            t += mods.count(2)/2
            r = mods.count(2) % 4
            a = mods.count(1)
            b = mods.count(3)
            d = abs(a-b)
            t += min(a, b)
            r2 = 1 if d % 4 else 0
            r = int(r or r2)
            return t + d/4 + r


class Chocolate(Solution):
    def parse_input(self):
        with open(self.input_file) as f:
            t = int(f.readline().strip())
            self.inputs = []
            for _ in range(t):
                n, p = [int(c) for c in f.readline().split()]
                gs = [int(c) for c in f.readline().split()]
                self.inputs.append(Case(n, p , gs))
    
    def run(self):
        self.results = [case.small_solve() for case in self.inputs]


Chocolate("A-small-attempt2")
