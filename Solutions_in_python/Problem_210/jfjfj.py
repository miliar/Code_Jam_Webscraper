t = int(raw_input().strip())
for i in range(1, t+1):
    c, d = list(map(int, raw_input().strip().split()))
    arr = []
    for j in range(0, c):
        a, b = list(map(int, raw_input().strip().split()))
        arr.append([a, b, "C"])
    for j in range(0, d):
        a, b = list(map(int, raw_input().strip().split()))
        arr.append([a, b, "J"])
    arr.sort()
    mi = arr[0][0]
    for j in range(0, len(arr)):
        arr[j][0] -= mi
        arr[j][1] -= mi
    ch = 0
    dc = 0
    dj = 0
    ud = 0
    pc = []
    pj = []
    tpc = 0
    tpj = 0
    for j in range(0, len(arr)-1):
        if arr[j][2] == "C":
            dc += arr[j][1]-arr[j][0]
        else:
            dj += arr[j][1]-arr[j][0]
        if arr[j][2] != arr[j+1][2]:
            ud += arr[j+1][0]-arr[j][1]
            ch += 1
        else:
            if arr[j][2] == "C":
                pc.append(arr[j+1][0]-arr[j][1])
                tpc += (arr[j+1][0]-arr[j][1])
            else:
                pj.append(arr[j+1][0]-arr[j][1])
                tpj += (arr[j+1][0]-arr[j][1])
    j = len(arr)-1
    if arr[j][2] == "C":
        dc += arr[j][1] - arr[j][0]
    else:
        dj += arr[j][1] - arr[j][0]
    if arr[j][2] != arr[0][2]:
        ud += 1440 - arr[j][1]
        ch += 1
    else:
        if arr[j][2] == "C":
            pc.append(1440 - arr[j][1])
            tpc += (1440 - arr[j][1])
        else:
            pj.append(1440 - arr[j][1])
            tpj += (1440 - arr[j][1])
    if dc+tpc > 720:
        trans = dc+tpc-720
        pc.sort()
        while trans > 0:
            trans -= pc[len(pc)-1]
            pc = pc[0:len(pc)-1]
            ch += 2
    elif dj+tpj > 720:
        trans = dj + tpj - 720
        pj.sort()
        while trans > 0:
            trans -= pj[len(pj) - 1]
            pj = pj[0:len(pj)-1]
            ch += 2
    else:
        pass
    print("Case #"+str(i)+": "+str(ch))
