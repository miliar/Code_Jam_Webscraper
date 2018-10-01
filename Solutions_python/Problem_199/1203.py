flip = {'+': '-', '-': '+'}


n = int(input())
i = 0

while i < n:
    i += 1
    count = 0

    start = input().split(' ')
    size = int(start[1])
    start = list(start[0])
    ok = True

    for j in range(len(start)):

        if start[j] == '-':
            count += 1

            if j + size > len(start):
                print("Case #" + str(i) + ": IMPOSSIBLE")
                ok = False
                break;

            for k in range(size):
                start[j+k] = flip[start[j+k]]
    if ok:
        print("Case #" + str(i) + ": " + str(count))

