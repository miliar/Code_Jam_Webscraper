#!/usr/bin/env python

def flatten(l):
    return [item for sublist in l for item in sublist]

def transpose(l):
    return [[row[x] for row in l] for x in range(len(l[0]))]

def can_mow(lawn, pattern):
    transposed_pattern = transpose(pattern)
    max_height = max(flatten(pattern))

    for height in range(max_height, -1, -1):
        for y, row in enumerate(pattern):
            if height in row and all([square <= height for square in row]): # confirm that the row needs mowing *and* can be mowed
                for x, square in enumerate(row):
                    if lawn[y][x] > height:
                        lawn[y][x] = height
        for x, col in enumerate(transposed_pattern):
            if height in col and all([square <= height for square in col]): # confirm that the column needs mowing *and* can be mowed
                for y, square in enumerate(col):
                    if lawn[y][x] > height:
                        lawn[y][x] = height

    return lawn == pattern

def make_lawn(y, x, initial_height=100):
    lawn = []
    for i in range(y):
        lawn.append([initial_height]*x)
    return lawn

def main():
    import sys
    num_test_cases = int(next(sys.stdin).strip())
    for i in range(num_test_cases):
        height, width = map(int, next(sys.stdin).split())
        pattern = list([list(map(int, next(sys.stdin).split())) for j in range(height)])
        sys.stdout.write("Case #{0}: {1}\n".format(i+1, "YES" if can_mow(make_lawn(height, width), pattern) else "NO"))


if __name__ == "__main__":
    main()
