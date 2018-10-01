#!/usr/bin/env python
import argparse


def is_tidy(n):
    n = str(n)
    for i in range(1, len(n)):
        if int(n[i]) < int(n[i-1]):
            return False
    return True


def next_tidy(n):
    if is_tidy(n):
        return n
    n = list(str(n))
    for i in reversed(range(1, len(n))):
        if int(n[i]) < int(n[i-1]):
            while n[i-1] == '0':
                i -= 1
            n[i-1] = str(int(n[i-1]) - 1)
            for x in range(i, len(n)):
                n[x] = '9'
            n = int(''.join(n))
            break
    return next_tidy(n)


def main(infile, outfile):
    with open(infile, 'r') as input, open(outfile, 'w') as out:
        num_cases = int(input.readline())
        for case in range(1, num_cases+1):
            out.write('Case #{}: '.format(case))

            N = int(input.readline().rstrip())

            n = next_tidy(N)
            out.write(str(n) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="codejam qual B")
    parser.add_argument('-i', '--input', type=str,
                        help='Input file')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file')
    args = parser.parse_args()
    main(args.input, args.output)
