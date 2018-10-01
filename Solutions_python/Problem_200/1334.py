from sys import stdin

def solve(n):
    lst = list(map(int, str(n)))

    for i in range(len(lst)-1, 0, -1):
        if lst[i-1] > lst[i]:
            lst[i:] = [9]*(len(lst)-i)
            lst[i-1] -= 1

        i -= 1

    return int("".join(map(str, lst)))

T = int(next(stdin))

for t in range(1, T+1):
    print("Case #{0}: {1}".format(t, solve(int(next(stdin)))))
