def find_next(arr, LS_arr, RS_arr):
    maxx = None
    min_arr = []

    for i in range(len(LS_arr)):
        if arr[i] == 1:
            continue

        if maxx == None or min(LS_arr[i], RS_arr[i]) > maxx:
            maxx = min(LS_arr[i], RS_arr[i])
            min_arr = [i]
        elif min(LS_arr[i], RS_arr[i]) == maxx:
            min_arr.append(i)

    maxx = None
    maxx_arr = []
    for i in min_arr:
        if maxx == None or max(LS_arr[i], RS_arr[i]) > maxx:
            maxx = max(LS_arr[i], RS_arr[i])
            maxx_arr = [i]
        elif max(LS_arr[i], RS_arr[i]) == maxx:
            maxx_arr.append(i)

    return maxx_arr[0]

T = int(raw_input())

for t in xrange(T):
    N, K = map(int, raw_input().split(" "))

    LS_arr = range(N)
    RS_arr = range(N-1, -1, -1)
    arr = [0] * N

    for k in xrange(K):
        index = find_next(arr, LS_arr, RS_arr)
        maxx = max(LS_arr[index], RS_arr[index])
        minn = min(LS_arr[index], RS_arr[index])
        arr[index] = 1

        for i in range(index - 1, -1, -1):
            if arr[i] == 1:
                break
            RS_arr[i] = index - i - 1
        for i in range(index + 1, N):
            if arr[i] == 1:
                break
            LS_arr[i] = i - index - 1

    print 'Case #' + str(t+1) + ": " + str(maxx) + " " + str(minn)
