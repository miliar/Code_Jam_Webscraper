import sys
import math


def main():
    t = int(sys.stdin.readline())
    for r in range(t):
        sys.stdin.readline()
        numbers = sorted(map(int, sys.stdin.readline().split()), reverse=True)

        m = numbers[0]
        result = m
        for k in range(1, m + 1):
            additional_moves = 0
            for x in numbers:
                if x > k:
                    additional_moves += int(math.ceil(1.0 * x / k)) - 1
            result = min(result, k + additional_moves)

        print ('Case #%d: %d' % (r + 1, result))

if __name__ == '__main__':
    main()
