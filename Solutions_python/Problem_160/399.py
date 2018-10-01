#!/usr/bin/python3

import sys
import fractions


def lcm(a, b):
    return int(abs(a * b) / fractions.gcd(a, b)) if a and b else 0


if __name__ == '__main__':
    test_count = int(sys.stdin.readline())

    for test_id in range(1, test_count + 1):
        b, pos = tuple(map(int, sys.stdin.readline().split()))
        b_time = list(map(int, sys.stdin.readline().split()))
        pos = pos - 1
        wait_time = [0 for x in b_time]

        reset_time = b_time[0]
        for t in b_time:
            reset_time = lcm(reset_time, t)
        period = 0
        for t in b_time:
            period += (reset_time // t)

        pos = pos % period

        last_position = -1
        for i in range(pos + 1):
            min_time = 999999
            last_position = -1
            for j in range(b):
                min_time = min(min_time, wait_time[j])
                if wait_time[j] == 0:
                    wait_time[j] = b_time[j]
                    last_position = j
                    break

            if min_time > 0:
                for j in range(b):
                    w = wait_time[j]
                    if last_position < 0 and w == min_time:
                        last_position = j
                        wait_time[j] = b_time[j]
                    else:
                        wait_time[j] = w - min_time

        print('Case #%d: %d' % (test_id, last_position + 1))
