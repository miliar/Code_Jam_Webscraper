def solve():
    N,K = [int(v) for v in input().split()]
    U = float(input())
    arr = [float(v) for v in input().split()]
    arr = sorted(arr)
    d = []
    for i in range(1,N):
        d.append(arr[i]-arr[i-1])
    i = 0
    s = 0
    while i < N-1 and s+(i+1)*d[i] <= U:
        s += (i+1)*d[i]
        i += 1
    pp(arr)
    ss = 0
    for j in range(i):
        # U -= (arr[i]-arr[j])
        ss += (arr[i]-arr[j])
        arr[j] = arr[i]
    U -= s
    pp(arr)
    ext = U / (i+1)
    for j in range(i+1):
        arr[j] += ext
        U -= ext
    pp(arr)
    prod = 1
    for i in range(N):
        prod *= arr[i]
    return min(prod,1)
        
def pp(arr):
    return
    print(','.join('%.3f' % v for v in arr))

T = int(input())
for t in range(1, T + 1):
    print('Case #%d: %.9f' % (t,solve()))


