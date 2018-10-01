import sys

def solve_problem(r, c, w):
    score = c / w + w - 1 + (c % w > 0) + (r - 1) * (c / w)
    return score

if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        r, c, w = map(int, sys.stdin.readline().split())
        print "Case #{0}: {1}".format(i, solve_problem(r, c, w))
