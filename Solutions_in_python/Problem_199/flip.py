from mybitarray import bitarray
from bfs import bfs, traversed_length

def is_complete(row):
    return row.count(False) == 0

def make_goal(row):
    return bitarray('1' * len(row))

def to_mask(k):
    return to_binary('1' * k)

def all_masks(row, k):
    num_zeros = len(row) - k

    masks = []
    for i in range(num_zeros + 1):
        left = i
        right = num_zeros - left
        masks.append(bitarray("%s%s%s" % ('0' * left, '1' * k, '0' * right)))

    return masks

def to_binary(s):
    s = s.replace("-", '0')
    s = s.replace("+", '1')
    return bitarray(s)

def solve(row, k):
    row = to_binary(row)
    goal = make_goal(row)
    if row == goal:
        return 0
    path = bfs(row, goal, all_masks(row, k))
    if path is not None:
        return traversed_length(path)

def main():
    # read a line with a single integer
    t = int(input())
    for i in range(1, t + 1):
        # read a list of integers, 2 in this case
        row, k = [s for s in input().split(" ")]
        answer = solve(row, int(k))
        if answer is None:
            answer = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, answer))

if __name__ == '__main__':
    main()
