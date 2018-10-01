"""

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible.

To avoid confusion, they follow deterministic rules:

For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively.
Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal.
If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal.
If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset.
You must solve the first Small dataset before you can attempt the second Small dataset.
You will be able to retry either of the Small datasets (with a time penalty).
You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.

Output

For each test case, output one line containing Case #x: y z,

where x is the test case number (starting from 1),
y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

Limits

1 ≤ T ≤ 100.
1 ≤ K ≤ N.
Small dataset 1

1 ≤ N ≤ 1000.
Small dataset 2

1 ≤ N ≤ 106.
Large dataset

1 ≤ N ≤ 1018.
"""


def distance_nearest_left_occupied(stalls, stall_i):
    nearest_left = None
    for i in range(stall_i - 1, -1, -1):
        if stalls[i]:
            nearest_left = i
            break
    return stall_i - nearest_left - 1


def distance_nearest_right_occupied(stalls, stall_i):
    nearest_right = stalls.index(True, stall_i + 1)
    return nearest_right - stall_i - 1


def occupy_stall(stalls, last=False):
    min_dist = None
    max_dist = None
    index = []
    for i in range(0, N + 2):
        if stalls[i]:
            continue
        s_L = distance_nearest_left_occupied(stalls, i)
        s_R = distance_nearest_right_occupied(stalls, i)
        if min_dist is None:
            min_dist = min(s_L, s_R)
            max_dist = [max(s_L, s_R)]
            index = [i]
        elif min_dist < min(s_L, s_R):
            min_dist = min(s_L, s_R)
            max_dist = [max(s_L, s_R)]
            index = [i]
        elif min_dist == min(s_L, s_R):
            max_dist.append(max(s_L, s_R))
            index.append(i)
    max_of_max_sL_sR = max(max_dist)
    # get maximal
    chosen_one = min([(x, y) for x, y in (zip(index, max_dist)) if y == max_of_max_sL_sR])
    stalls[chosen_one[0]] = True
    if last:
        return max_of_max_sL_sR, min_dist
    return stalls


def stall_simulation(N, K):
    occupied = True
    total_stalls = N + 2
    stalls = [False for _ in range(total_stalls)]
    stalls[0] = stalls[len(stalls) - 1] = occupied
    for i in range(K):
        if i == K - 1:
            return occupy_stall(stalls, last=True)
        stalls = occupy_stall(stalls)


with open('C-small-1-attempt0.in') as f:
    lines = f.read().split('\n')
    cases = int(lines[0])
    case_number = 1
    for x in lines[1:]:
        inp = x.split(' ')
        N, K = int(inp[0]), int(inp[1])
        y, z = stall_simulation(N, K)
        print("Case #%d: %d %d" % (case_number, y, z))
        case_number += 1
