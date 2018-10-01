__author__ = 'ar'
import sys

def is_possible(cnts):
    s = 0
    for s_i, cnt in cnts:
        if s < s_i:
            return False
        s += cnt

    return True

def solve(cnts):
    min_p = 0
    max_p = len(cnts)

    while min_p < max_p:
        mid = (min_p + max_p) / 2
        old_tup = cnts[0]
        new_tup = old_tup[0], old_tup[1] + mid
        cnts[0] = new_tup
        if is_possible(cnts):
            max_p = mid
        else:
            min_p = mid + 1
        cnts[0] = old_tup
    return min_p


if __name__ == "__main__":
    lines = sys.stdin.read().split("\n")
    t = int(lines.pop(0).strip())
    for idx in range(0, t):
        l = lines[idx]
        parts = l.split(' ')
        cnts = [(s_i, int(c)) for s_i, c in enumerate(parts[1])]
        res = solve(cnts)
        print "Case #%d: %d" % (idx + 1, res)

