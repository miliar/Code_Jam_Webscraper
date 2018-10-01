import math
import sys
#sys.setrecursionlimit(10000)

def find_closest(activ, time):
    for i, e in enumerate(activ):
        if e[1] > time:
            return i

    return -1

def solve_recur(c_activ, k_activ, time, c_turn, c_rem_time, k_rem_time):

    if time >= 1440 and c_rem_time == 0 and k_rem_time == 0:
        return 0
    if time > 1440*2:
        return 2**63

    if c_turn:
        closest = find_closest(c_activ, time)
        closest2 = find_closest(k_activ, time)
        max_time = c_rem_time if closest == -1 or c_activ[closest][0] - time > c_rem_time else c_activ[closest][0] - time
        max_time2 = c_rem_time if closest2 == -1 or k_activ[closest2][0] - time > c_rem_time else k_activ[closest2][0] - time
    else:
        closest = find_closest(k_activ, time)
        closest2 = find_closest(c_activ, time)
        max_time = k_rem_time if closest == -1 or k_activ[closest][0] - time > k_rem_time else k_activ[closest][0] - time
        max_time2 = k_rem_time if closest2 == -1 or c_activ[closest2][0] - time > k_rem_time else c_activ[closest2][0] - time

    if max_time == 0 and max_time2 == 0:
        return 2**63
    return 1 + min(solve_recur(c_activ, k_activ, time + max_time, not c_turn, c_rem_time - max_time, k_rem_time - max_time),
                   solve_recur(c_activ, k_activ, time + max_time2, not c_turn, c_rem_time - max_time2, k_rem_time - max_time2))

def solve(c_activ, k_activ):
    c_activ.sort(key=lambda tup: tup[0])
    k_activ.sort(key=lambda tup: tup[0])
    for (a, b) in list(c_activ):
        c_activ.append((a + 1440, b +1440))
    for (a, b) in list(k_activ):
        k_activ.append((a + 1440, b + 1440))

    swaps = 2**64
    for start_c in range(720):
        swaps = min(solve_recur(c_activ, k_activ, start_c, True, 12*60, 12*60), swaps)
    for start_k in range(720):
        swaps = min(solve_recur(c_activ, k_activ, start_k, False, 12*60, 12*60), swaps)

    return swaps


def main():
    t = int(input())
    for i in range(1, t + 1):
        c, k = [int(s) for s in input().split(" ")]
        c_activ = []
        k_activ = []
        for j in range(c):
            c_activ.append([int(s) for s in input().split(" ")])
        for j in range(k):
            k_activ.append([int(s) for s in input().split(" ")])

        print(f"Case #{i}: {solve(c_activ, k_activ)}")


if __name__ == "__main__": main()