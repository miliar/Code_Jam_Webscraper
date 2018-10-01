from __future__ import print_function

import fractions
import sys

def calc(S, K):
    n = len(S)
    num_moves = n - K + 1
    num_flips = 0
    state = list(S)


    for i in range(num_moves):
        if state[i] == '+':
            continue
        # Do flips.
        num_flips += 1
        for j in range(K):
            pos = i + j
            state[pos] = '-' if state[pos] == '+' else '+'

    # Check.
    right =  state[-K:]
    if '-' in right:
        return 'IMPOSSIBLE'

    return num_flips

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        S, K = f.readline().strip().split()
        K = int(K)
        assert 2 <= K <= len(S), '{} {}'.format(K, len(S))

        r = calc(S, K)

        print('Case #{}: {}'.format(case_id, r))

if __name__ == '__main__':
    main()
    # do_stuff()
