import sys
import numpy as np

def read_case(line):
    status, flips = tuple(line.strip().split(" "))
    status = np.array([True if s == "+" else False for s in status])
    return status, int(flips)


def make_solution(case):
    status, flips = case
    num_flipped = 0

    for i in range(len(status) - flips + 1):
        if status[i]:
            continue
        status[i:i+flips] = ~ status[i:i+flips]
        num_flipped += 1

    if all(status):
        return num_flipped
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    f = sys.stdin
    # f = open("samples.text")
    count = int(f.readline())
    for c in range(count):
        case_c = read_case(f.readline())
        solution = make_solution(case_c)
        print("Case #{}: {}".format(c+1, solution))