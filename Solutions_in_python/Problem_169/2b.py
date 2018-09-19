"""Solve the '2B' problem (GCJ 2015)."""

from solver import solver


def solve(v, x, l):
    r0, c0 = l[0]
    if len(l) == 1:
        if c0 != x:
            return "IMPOSSIBLE"
        return v/r0
    r1, c1 = l[1]
    if c0 == c1:
        return solve(v, x, [(r0+r1, c0)])
    v0 = v * (x - c1) / (c0 - c1)
    v1 = v * (x - c0) / (c1 - c0)
    if v0 < 0 or v1 < 0:
        return "IMPOSSIBLE"
    return max(v0/r0, v1/r1) 


@solver(lines_per_case="args[0]")
def gcj_2b(lines):
    _, v, x = map(float, lines[0].split())
    l = [map(float, line.split()) for line in lines[1:]]
    return solve(v, x, l)


if __name__ == "__main__":
    gcj_2b.from_cli()
