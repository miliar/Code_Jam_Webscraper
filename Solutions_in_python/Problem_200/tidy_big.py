t = int(input())
res = []
for i in range(t):
    k = int(input())
    temp = list(map(int, list(str(k))))
    asc = False
    while not asc:
        asc = True
        for l in range(temp.__len__() - 1):
            if temp[l] > temp[l + 1]:
                asc = False
                temp[l] -= 1
                for ll in range(l + 1, temp.__len__()):
                    temp[ll] = 9
    res.append(int(''.join(list(map(str, temp)))))

for i in range(res.__len__()):
    print("Case #" + str(i + 1) + ": " + str(res[i]))
