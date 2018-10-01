import sys
import blist


def parse_input(fil):
    fil.readline()
    return map(int, fil.readline().split())


def solve(agg):
    best = 10000
    special = 0
    while True:
        num, count = agg.popitem()
        best = min(best, num + special)
        if num <= 3:
            break

        special += count
        new = num // 2
        agg[new] = agg.get(new, 0) + count
        agg[num - new] = agg.get(num - new, 0) + count

    return best


def solution(counts):
    agg = blist.sorteddict(lambda x: -x)
    for elem in counts:
        agg[elem] = agg.get(elem, 0) + 1

    best = 10000
    if next(agg.iterkeys()) >= 9:
        cop = blist.sorteddict(agg)
        num, count = cop.popitem()
        cop[num // 3] = cop.get(num // 3, 0) + 3 * count
        best = count * 2 + solve(cop)
    return min(solve(agg), best)


def main():
    n = int(sys.stdin.readline())
    sys.stdout.writelines('Case #%d: %d\n' % (i + 1,
                                              solution(parse_input(sys.stdin)))
                          for i in xrange(n))


if __name__ == '__main__':
    main()
