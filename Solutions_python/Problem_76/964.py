import sys

numbers = [1, 2, 3, 4, 5, None]

"""
# 5
1 | 2 3 4 5
2 | 1 3 4 5
3 | 1 3 4 5
4 | 1 2 3 5
5 | 1 2 3 4

# 4
1 2 | 3 4 5
1 3 | 2 4 5
1 4 | 2 3 5
1 5 | 2 3 4

# 3
1 2 3 | 4 5
1 2 4 | 3 5
1 2 5 | 3 4

# 2
1 2 3 4 | 5
1 2 3 5 | 4

# 1
1 2 3 4 5
"""

# The pattern
def solve(original, case):
    lhs_size = 1
    rhs_size = len(original) - 1

    if len(original) == 2 and original[0] == original[1]:
        print "Case #%d: %d" % (case, original[0])
        return

    max_found = 0
    while lhs_size < len(original) - 1:
        n = original[:]
        combinations = []
        lhs_keep = n[:lhs_size - 1]
        for i in range(lhs_size - 1, rhs_size + 1):
            l = lhs_keep[:]
            l.append(n[i])
            combinations.append((l, i))
        for lhs, d in combinations:
            rhs = n[:]
            del rhs[d]
            del rhs[:lhs_size - 1]
            lhs_xor = 0; rhs_xor = 0
            lhs_sum = 0; rhs_sum = 0
            for i in lhs:
                lhs_xor ^= i
                lhs_sum += i
            for i in rhs:
                rhs_xor ^= i
                rhs_sum += i
            if lhs_xor == rhs_xor:
                #print "Possible match: (%s, %s), (%s, %s)" % (lhs_sum, lhs_xor, rhs_sum, rhs_xor)
                if lhs_sum > max_found:
                    max_found = lhs_sum
                if rhs_sum > max_found:
                    max_found = rhs_sum
        lhs_size += 1
    if max_found != 0:
        print "Case #%d: %d" % (case, max_found)
    else:
        print "Case #%d: NO" % (case)

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    tests = int(lines[0])
    cases = 1
    for i in range(2, tests * 2 + 1, 2):
        original = map(int, lines[i].split())
        solve(original, cases)
        cases += 1

