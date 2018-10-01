import re as regex

tc = int(input())
for tt in range(tc):
    row, col = map(int, input().split())
    arr = []
    for i in range(row):
        arr.append(list(input()))
    for i in range(row):
        for j in range(col):
            if arr[i][j] != "?":
                for k in range(j - 1, -1, -1):
                    if arr[i][k] == "?":
                        arr[i][k] = arr[i][j]
                    else:
                        break
        for j in range(col - 1, -1, -1):
            if arr[i][j] != "?":
                break
        for k in range(j + 1, col):
            arr[i][k] = arr[i][j]
    for i in range(row):
        if len(regex.findall(r"\?{%d}" % col, "".join(arr[i]))) == 0:
            for j in range(i - 1, -1, -1):
                if len(regex.findall(r"\?{%d}" % col, "".join(arr[j]))) != 0:
                    arr[j] = arr[i]
                else:
                    break
    for i in range(row - 1, -1, -1):
        if len(regex.findall(r"\?{%d}" % col, "".join(arr[i]))) == 0:
            break
    for j in range(i + 1, row):
        arr[j] = arr[i]
    print("Case #%d:" % (tt + 1))
    for i in range(row):
        print("".join(arr[i]))