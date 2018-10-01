import sys

import math

def square(x):
    root = math.sqrt(x)
    floor = math.floor(root)
    if floor == root:
        return floor

    return None

def fair(x):
    s = str(x)

    i = 0
    j = len(s)-1
    while i<=j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def count_fair_and_square(start, end):
    count = 0
    for i in range(start, end + 1):
        if fair(i):
            s = square(i)
            if s is not None and fair(s):
                count += 1

    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s input_file".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file + ".out"
    with open(input_file) as input:
        with open(output_file, "wt") as output:
            T = int(input.readline().strip())

            for i in range(T):
                interval = input.readline().strip().split()
                A = int(interval[0])
                B = int(interval[1])

                count = count_fair_and_square(A,B)

                output.write("Case #{}: {}".format(i+1, count))

                output.write("\n")