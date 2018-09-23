


def generic_function(n, m, cake):
    a = 0
    b = 0
    for _ in range(n):
        for a in range(n):
            for b in range(m):
                if cake[a][b] == '?':
                    if a > 0 and cake[a-1][b] != '?':
                        cake[a][b] = cake[a-1][b]
                    elif a < n - 1 and cake[a+1][b] != '?':
                        cake[a][b] = cake[a+1][b]
    for _ in range(m):
        for a in range(n):
            for b in range(m):
                if cake[a][b] == '?':
                    if b > 0 and cake[a][b-1] != '?':
                        cake[a][b] = cake[a][b-1]
                    elif b < m - 1 and cake[a][b+1] != '?':
                        cake[a][b] = cake[a][b+1]
    return cake



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]

    strings = []
    for _ in range(n):
        strings.append(list(input()))

    fixed_cake = generic_function(n, m, strings)
    total = []
    for a in range(n):
        string = ""
        for b in range(m):
            string += fixed_cake[a][b]
        total.append(string)

    print("Case #{}:".format(i, ))
    for i in total:
        print(i)
