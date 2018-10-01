
from heapq import *

def brute_test():

    print '_ ',
    for i in xrange(1, 20):
        print str(i) + " ",
    print

    for j in xrange(1, 20):

        res = [0] * 20

        h = [-j]
        for idx in xrange(j):

            first       = -heappop(h)
            res[first] += 1

            #  split
            if first % 2 == 0:
                l, r = first / 2 - 1, first / 2
            else:
                l, r = first / 2, first / 2

            if l != 0:
                heappush(h, -l)

            if r != 0:
                heappush(h, -r)

        print j, res[1:]


# brute_test()
# exit(0)

def brute(n, k):

    h    = [-n]
    l, r = 0, 0

    for idx in xrange(k):

        first = -heappop(h)

        #  split
        if first % 2 == 0:
            l, r = first / 2 - 1, first / 2
        else:
            l, r = first / 2, first / 2

        if l != 0:
            heappush(h, -l)

        if r != 0:
            heappush(h, -r)

        # print idx + 1, ":", h

    return str(max(l, r)) , str(min(l, r))


def split(n):

    if n % 2 == 0:
        left, right = n / 2 - 1, n / 2
    else:
        left, right = n / 2, n / 2

    return left, right


def ans(left, right):
    return str(max(left, right)), str(min(left, right))

from collections import defaultdict
from orderedset import OrderedSet


def lgn(n, k):

    h    = defaultdict(int)
    nums = OrderedSet()

    left, right = split(n)

    csum = 0

    nums.add(n)
    h[n] = 1

    while csum < k:

        item        = nums[0]
        left, right = split(item)

        # print "lr:", left, right

        if item == 1:
            left, right = 0, 0
            break

        nums = nums[1:]
        count = h[item]
        nums.add(right)
        h[right] += count

        nums.add(left)
        h[left] += count

        csum += count

        # print csum, k

    return str(max(left, right)), str(min(left, right))


def solve_test(line, g):

    n, k = map(int, line.split())

    # bn, bk = brute(n, k)
    # g.write(bn + " " + bk)

    tn, tk = lgn(n, k)
    g.write(tn + " " + tk)

    # print n, k, ": ", bn, bk, "|", tn, tk
    # exit(0)


def solve(file):

    with open(file) as f:
        with open("res", "w") as g:
            for idx, line in enumerate(f.readlines()[1:]):
                g.write("Case #" + str(idx + 1) + ": ")
                solve_test(line, g)
                g.write("\n")


def main():
    solve("C-large.in")
    # solve("B-large.in")


if __name__ == "__main__":
    main()

