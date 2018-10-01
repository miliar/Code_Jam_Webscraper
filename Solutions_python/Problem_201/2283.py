import sys
import numpy as np
import numpy.ma as ma
import math
from heapq import *

def read_case(line):
    N, K = line.strip().split()
    return int(N), int(K)


def make_solution(case):
    N, K = case
    increasing = np.array(list(range(N)))
    decreasing = np.array(increasing[::-1])

    # status variables
    free = np.ones(N, dtype=bool)
    left = np.zeros(N, dtype=int)
    right = np.zeros(N, dtype=int)

    # init with initial distances
    left[0:N] = increasing
    right[0:N] = decreasing

    for k in range(K):
        # print("customer {}".format(k))
        # mask with current occupancy status
        left = ma.array(left, mask=~free)
        right = ma.array(right, mask=~free)
        #print("left",left)
        #print("right", right)

        mins = ma.minimum(left, right)
        maxs = ma.maximum(left, right)
        #print("mins", mins)
        #print("maxs", maxs)

        # candidates are all stalls where mins are maximal
        max_mins = mins.max()
        candidates = ma.where(mins == max_mins)[0]
        #print(max_mins, candidates)

        # from those candidates select the one where max is also maximal
        selected = ma.argmax(maxs[candidates])
        selected = candidates[selected]
        #print(selected)

        # occupy stall and update left and right
        free[selected] = False
        if selected > 0:
            # left of selected, right distance has to be updated
            right[0:selected] = ma.minimum(decreasing[-selected:], right[0:selected])
        if selected < N -1:
            # right of selected, left distance has to be updated
            left[selected+1:] = ma.minimum(increasing[:N-selected -1], left[selected+1:])

        if k == K -1:
            return maxs[selected], mins[selected]


def make_solution_fast(case):
    N, K = case

    queue = []
    heapify(queue)
    heappush(queue, -N)

    for k in range(K-1):
        cur = - heappop(queue)

        if cur % 2 == 0:
            spaces_to_the_left = int(math.floor((cur - 1)/2.0))
            spaces_to_the_right = int(math.ceil((cur - 1) / 2.0))
        else:
            spaces_to_the_left = int(math.floor((cur - 1) / 2.0))
            spaces_to_the_right = int(math.floor((cur - 1) / 2.0))

        if spaces_to_the_left > 0:
            heappush(queue, - spaces_to_the_left)
        if spaces_to_the_right > 0:
            heappush(queue, - spaces_to_the_right)

    cur = - heappop(queue)
    d_max = math.floor(cur / 2.0)
    d_min = math.floor((cur - 1) / 2.0)
    return max(d_max, 0), max(d_min, 0)

if __name__ == "__main__":
    f = sys.stdin
    # f = open("samples.text")
    count = int(f.readline())
    for c in range(count):
        case_c = read_case(f.readline())
        solution = make_solution_fast(case_c)

        # for debugging
        #solution_slow = make_solution(case_c)
        #if solution[0] != solution_slow[0] or solution[1] != solution_slow[1]:
        #    print(solution, solution_slow)
        #    raise Exception("Fail at case {}".format(c+1))

        print("Case #{}: {} {}".format(c+1, solution[0], solution[1]))


