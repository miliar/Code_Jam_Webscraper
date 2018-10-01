#!/usr/bin/env python3

import sys
import re


def read():
    return sys.stdin.readline().strip()


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def complete_cake(cake):
    for direction in range(2):
        for row in cake:
            for index in range(len(row)):
                if index > 0 and row[index] == '?' and row[index-1] != '?':
                    copy_character_right(row, index-1)
                if index < len(row) - 1 and row[index] == '?' and row[index+1] != '?':
                    copy_character_left(row, index+1)

        cake = transpose(cake)

    return cake


def copy_character_right(row, index):
    while index < len(row) - 1 and row[index+1] == '?':
        row[index+1] = row[index]
        index += 1


def copy_character_left(row, index):
    while index > 0 and row[index-1] == '?':
        row[index-1] = row[index]
        index -= 1


def main():
    num_cases = int(read())
    for case in range(num_cases):
        rows, cols = [int(x) for x in read().split(" ")]

        cake = []
        for r in range(rows):
            row = list(read())
            cake.append(row)

        cake = complete_cake(cake)

        print("Case #{}:".format(case+1))
        for row in cake:
            print("".join(row))


if __name__ == '__main__':
    main()

