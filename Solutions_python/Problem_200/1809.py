# codejam
from sys import stdin


# Solver
def solve(N):
    s = str(N)
    n = N
    inc = True
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            inc = False
            for j in range(i, -1, -1):
                if (s[j] > s[j - 1] or j == 0):
                    n = int(s[0:j + 1])
                    n *= pow(10, len(s) - j - 1)
                    break
            break

    if not inc:
        return n - 1
    else:
        return n

# I/O
T = int(stdin.readline())

for t in range(0, T):
    N = int(stdin.readline())
    print('Case #{0}: {1}'.format(t + 1, solve(N)))
