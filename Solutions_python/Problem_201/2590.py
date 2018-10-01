c = int(raw_input())

for idx in range(c):
    n, k = raw_input().split()
    n, k = int(n), int(k)

    arr = [n]
    for i in range(k-1):
        m = max(arr)
        pos = arr.index(m)
        if m % 2 == 0:
            arr.insert(pos, m/2-1)
        else:
            arr.insert(pos, m/2)
        arr[pos+1] = m/2

    m = max(arr)
    m1, m2 = (m/2, m/2-1) if m % 2 == 0 else (m/2, m/2)
    print "Case #{}: {} {}".format(idx+1, m1, m2)
