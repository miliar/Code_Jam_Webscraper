def solve(arr):
    n=0
    for i,v in enumerate(arr[1:], start=1):
        if arr[i-1] < i:
            diff = i - arr[i-1]
            n += diff
            arr[i-1] += diff
        arr[i] += arr[i-1]
    return n

T = int(input())
for case in range(T):
    Smax, str = input().split(' ')
    Smax = int(Smax)
    S = list(map(int,list(str)))
    number = solve(S)
    print("Case #", case+1, ': ', number, sep='')