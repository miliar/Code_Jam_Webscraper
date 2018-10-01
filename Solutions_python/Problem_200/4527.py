
T = int(input())

for i in range(T):
    N = int(input())

    for j in range(N, -1, -1):
        n = list(str(j))
        n_sort = sorted(n)

        if n == n_sort:
            print("Case #" + str(i+1) + ": " + str(j))
            break
        
