#!/usr/bin/env python

from __future__ import division, print_function
import sys


def is_tidy_number(X):
    if type(X) == int:
        X = list(map(int, str(X)))
    return all(X[i - 1] <= X[i] for i in range(1, len(X)))

def subtract(X, idx):
    if X[idx] == 0:
        if idx == 0:
            return X
        else:
            for i in range(idx, len(X)):
                X[i] = 9
            return subtract(X, idx - 1)
    else:
        X[idx] -= 1
        return X


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())

        if is_tidy_number(N):
            print('Case #%d: %s' % (i + 1, N))
        else:
            X = list(map(int, str(N - 1)))

            idx = 0

            while idx < len(X):
                if is_tidy_number(X[: idx + 1]):
                    idx += 1
                else:
                    X = subtract(X, idx)
                    idx = 0

            while X[0] < 1:
                X.pop(0)

            print('Case #%d: %s' % (i + 1, ''.join(map(str, X))))