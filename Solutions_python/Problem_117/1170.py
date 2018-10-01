#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Régis Décamps"
import sys


def is_lawned(matrix):
    for i in range(len(matrix)):
        line = matrix[i]
        for j in range(len(line)):
            x = line[j]
            # x est le plus grand sur sa ligne ou sa colonne
            if x == max(line) or x == max( (matrix[k][j] for k in range(len(matrix)))):
                pass
            else:
                return False
    return True

if __name__ == '__main__':
    #generate_palindromes(7)
    with open(sys.argv[1]) as f:
        nb_tests = int(f.readline())
        for i in range(1, nb_tests + 1):
            matrix = []
            n, m = f.readline().split(' ')
            n = int(n)
            for j in range(n):
                line = f.readline()
                matrix.append([int(x) for x in line.split(' ')])
            print("Case #{i}: {result}".format(i=i, result="YES" if is_lawned(matrix) else "NO"))
