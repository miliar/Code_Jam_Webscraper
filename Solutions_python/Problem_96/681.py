# dancing with the googlers
#
import sys
import math

# segment the problem space:
# dancers guaranteed to win, without requiring a surprise
# dancers guaranteed to lose, even with a surprise
# of the remaining dancers, at most S had surprise triplets and thus at most S could have a score of at least p

def main():
    tests = read_input()
    #import pprint; pprint.PrettyPrinter(indent=4, width=10).pprint(tests); return
    results = map(solve, tests)
    print_results(results)


def read_input():
    # read input from stdin
    lines = map(lambda line: line.strip('\n'), sys.stdin.readlines())

    # parse it out
    num_tests = int(lines[0])
    lines = lines[1:]

    tests = []
    for i in range(num_tests):
        tests += [map(int, lines[i].split())]

    return tests


def print_results(results):
    for i, r in enumerate(results):
        print 'Case #%d: %s' % (i + 1, r)


def solve(test):
    N, S, p = test[0:3]
    scores = test[3:]

    def min_best_score_without_surprise(x):
        return min(10, math.floor((x+2)/3.0))

    def best_poss_score(x):
        return min(10, x, math.floor((x+4)/3.0))

    winners = sum(1 for x in scores if p <= min_best_score_without_surprise(x))
    losers = sum(1 for x in scores if p > best_poss_score(x))
    left = N - winners - losers
    return winners + min(S, left)

main()
