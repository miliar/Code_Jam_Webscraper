#! /usr/bin/env python

import fractions
import math

def main():
    t = int(raw_input())
    for i in range(1, t + 1):
        a, b = raw_input().split('/')
        a = int(a)
        b = int(b)
        divisor = fractions.gcd(a, b)

        reduced_a = a / divisor
        reduced_b = b / divisor

        log = math.log(reduced_b, 2)
        if int(log) != log:
            # denominator of reduced fraction is not a power of 2
            answer = 'impossible'
        else:
            answer = (int(math.log(reduced_b,2))
                      - int(math.log(reduced_a,2)))

        print('Case #%i: %s' % (i, str(answer)))



if __name__ == '__main__':
    main()
