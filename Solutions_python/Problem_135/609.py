#!/usr/bin/env python

import sys

def find_number(row1, row2):
    row1_ints = set(int(i) for i in row1.split())
    row2_ints = set(int(i) for i in row2.split())
    intersect = row1_ints & row2_ints
    if not intersect:
        return "Volunteer cheated!"
    elif len(intersect) == 1:
        return str(intersect.pop())
    else:
        return "Bad magician!"


if __name__ == "__main__":
    results = []
    with open(sys.argv[1]) as f:
        cases = int(f.readline().strip())
        for _ in range(cases):
            row1_idx = int(f.readline().strip())
            for i in range(4):
                row = f.readline().strip()
                if i+1 == row1_idx:
                    row1 = row
            row2_idx = int(f.readline().strip())
            for i in range(4):
                row = f.readline().strip()
                if i+1 == row2_idx:
                    row2 = row
            results.append(find_number(row1, row2))
    for i, result in enumerate(results, start=1):
        print("Case #%d: %s" % (i, result))
