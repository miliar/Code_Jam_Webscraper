def foo(N):
    arr = [int(digit) for digit in N]
    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            for j in range(i, len(arr)):
                arr[j] = 9
            arr[i-1] = max(0, arr[i-1]-1)
    return int(''.join(map(str,arr)))

T = int(input())
for _ in range(T):
    N = str(input())
    print("Case #{}: {}".format(_+1, foo(N)))