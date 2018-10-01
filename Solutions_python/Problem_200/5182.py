#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

import sys
def main():
    filename = sys.argv[1]
    with open(filename, "r") as f:
        with open(filename.replace(".in", ".out"), "w") as f2:
            for i, line in enumerate(f.readlines()):
                if i != 0:
                    f2.write("Case #{}: {}\n".format(i, largest_tidy_number(int(line.strip()))))
def largest_tidy_number(n):
    for number in range(n, 0, -1):
        if is_tidy_number(str(number)):
            return number

def is_tidy_number(n):
    for i, dig in enumerate(n[:-1]):
        if dig > n[i+1]:
            return False
    return True

if __name__ == "__main__":
    main()





