T = int(input())


def solve(N):
    N = list(N)
    l = len(N)
    flg = False
    for i in range(l - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if N[j] > N[i]:
                N[j] = str(int(N[j]) - 1)
                for k in range(j + 1, l):
                    N[k] = "9"
                break
    if N[0] == "0":
        N = N[1:]
    return "".join(N)


for t in range(T):
    N = input()
    print("Case #{}: {}".format(t + 1, solve(N)))
