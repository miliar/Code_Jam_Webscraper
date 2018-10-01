import bisect
import decimal
import sys


if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        blocks = int(stdin.readline())

        line = stdin.readline()
        naomi = sorted(map(decimal.Decimal, line.split()))
        naomi_2 = naomi[:]

        line = stdin.readline()
        ken = sorted(map(decimal.Decimal, line.split()))
        ken_2 = ken[:]

        res = 0
        current = blocks
        for j in naomi:
            won = True
            pos = bisect.bisect_left(ken, j)
            if pos < current:
                won = False
                del ken[pos]
                current -= 1
            if won:
                res += 1

        r_res = 0
        current = blocks
        for k in ken_2:
            won = False
            pos = bisect.bisect_left(naomi_2, k)
            if pos < current:
                won = True
                del naomi_2[pos]
                current -= 1
            if won:
                r_res += 1

        print "Case #%d: %d %d" % (i+1, r_res, res)
