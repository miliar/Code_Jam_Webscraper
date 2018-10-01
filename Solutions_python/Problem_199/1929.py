#!/usr/bin/env python
import argparse


def flip(S, i, k):
    for p in reversed(range(i, i+k)):
        if S[p] == '+':
            S[p] = '-'
        else:
            S[p] = '+'
    return S


def main(infile, outfile):
    with open(infile, 'r') as input, open(outfile, 'w') as out:
        num_cases = int(input.readline())
        for case in range(1, num_cases+1):
            out.write('Case #{}: '.format(case))

            S, k = input.readline().rstrip().split()
            S = list(S)
            k = int(k)
            flips = 0
            for i, p in enumerate(S):
                if p == '-':
                    try:
                        S = flip(S, i, k)
                        flips += 1
                    except:
                        flips = 'IMPOSSIBLE'
                        break

            out.write(str(flips) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="codejam qual A")
    parser.add_argument('-i', '--input', type=str,
                        help='Input file')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file')
    args = parser.parse_args()
    main(args.input, args.output)
