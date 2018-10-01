import sys


class StandingOvation:

    def solve_case(self, f):
        m, a = f.readline().split(" ")
        m = int(m)
        a = map(int, a.rstrip())
        tot = 0
        needed = 0
        for i in range(m+1):
            if i > tot:
                additional = i - tot
                needed += additional
                tot += additional
            tot += a[i]
        return needed

    def create_report(self, ci, r):
        r = ", ".join(map(str, r)) if isinstance(r, (list, tuple)) else str(r)
        return "Case #" + str(ci) + ": " + r

    def solve(self, f):
        t = int(f.readline())
        results = []
        for c in range(t):
            results.append(self.solve_case(f))
        return "\n".join(map(lambda c: self.create_report(c[0] + 1, c[1]), enumerate(results)))

    def solve_and_save(self, out, f):
        out.write(self.solve(f))

if __name__ == "__main__":
    so = StandingOvation()

    if len(sys.argv) < 2:
        so.solve_and_save(sys.stdout, sys.stdin)
    else:
        f = open("./in/" + sys.argv[1] + ".in", 'r')
        o = open("./out/" + sys.argv[1] + ".out", 'w')
        so.solve_and_save(o, f)
        f.close()
        o.close()
