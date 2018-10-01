import sys

def solve(intervals_A, intervals_B):
    if not intervals_A and not intervals_B:
        return 2
    elif intervals_A and not intervals_B:
        if len(intervals_A) == 1 or can_cover(intervals_A, 720):
            return 2
        else:
            return 4
    elif intervals_B and not intervals_A:
        if len(intervals_B) == 1 or can_cover(intervals_B, 720):
            return 2
        else:
            return 4
    else:
        return 2

def can_cover(intervals, N):
    intervals = sorted(intervals)
    if intervals[1][0] + N >= 1440 + intervals[0][1] or intervals[0][0] + N >= intervals[1][1]:
        return True
    else:
        return False

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        A_c, A_j = map(int, sys.stdin.readline().split())
        Act_c = []
        Act_j = []
        for x in range(A_c):
            s, e = map(int, sys.stdin.readline().split())
            Act_c.append((s, e))
        for x in range(A_j):
            s, e = map(int, sys.stdin.readline().split())
            Act_j.append((s, e))
        print "Case #{}: {}".format(case + 1, solve(Act_c, Act_j))
