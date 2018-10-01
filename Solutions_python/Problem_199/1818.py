t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    count = 0
    l = input().split(" ")
    S, K = list(l[0]), int(l[1])
    for j in range(len(S)):
        if S[j] == "-":
            if j > len(S) - K:
                print("Case #{}: IMPOSSIBLE".format(i))
                count = 0
                break
            else:
                count += 1
                for k in range(K - 1):
                    if S[j + k + 1] == "-":
                        S[j + k + 1] = "+"
                    else:
                        S[j + k + 1] = "-"
        else:
            if j == len(S) - 1:
                print("Case #{}: {}".format(i, count))