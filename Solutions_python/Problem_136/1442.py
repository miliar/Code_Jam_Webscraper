import decimal
import sys


if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        line = stdin.readline()
        c, f, x = map(decimal.Decimal, line.split())

        minimum = x / 2
        max_farms = minimum / (c / 2)

        costs = {}
        total = {}
        for j in range(0, max_farms + 1):
            xs = x / (j*f + 2)
            if j == 0:
                costs[0] = 0
            else:
                costs[j] = costs[j - 1] + c / ((j - 1)*f + 2)
            total[j] = xs + costs[j]

        minimum = min(total.values())
        print "Case #%d: %f" % (i+1, minimum)

