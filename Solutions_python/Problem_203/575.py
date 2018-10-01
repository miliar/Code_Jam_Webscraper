def my_initial_approach(R, C):
    merge = []
    for row in range(R):
        s = input()
        i = 0
        for c in s:
            if c == '?':
                i +=1
        if i == C:
            merge.append(None)
        else:
            sl = list(s)
            # Each row gets a two-pass
            for i in range(0, len(sl)-1):
                if sl[i] != '?' and sl[i+1] == '?':
                    sl[i+1] = sl[i]
            for i in range(len(sl)-1, 0, -1):
                if sl[i] != '?' and sl[i-1] == '?':
                    sl[i-1] = sl[i]
            merge.append(''.join(sl))

    # Two pass merge rows
    for i in range(0, len(merge)-1):
        if merge[i] is not None and merge[i+1] is None:
            merge[i+1] = merge[i]

    for i in range(len(merge)-1, 0, -1):
        if merge[i] is not None and merge[i-1] is None:
            merge[i-1] = merge[i]

    return merge

T = int(input())
for t in range(1, T+1):
    R, C = input().split(' ')
    result = my_initial_approach(int(R), int(C))
    print('Case #', t, ':', sep='')
    for row in result:
        print(row)



