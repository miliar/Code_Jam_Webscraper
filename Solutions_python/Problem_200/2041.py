def tidy(s):
    arr = [int(c) for c in s]
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]: 
            arr[i] -= 1
            for j in range(i+1, len(s)):
                arr[j] = 9
            k = i - 1
            while k >= 0 and arr[k] > arr[k+1]:
                arr[k] -= 1 
                arr[k+1] = 9; k -= 1
            res, digit = 0, 1
            for j in range(len(arr)-1,-1,-1):
                res += arr[j] * digit
                digit *= 10
            return res
        i += 1
    return int(s)

T = int(input())
for t in range(T):
    s = input()
    res = tidy(s)
    print("Case #%i: %i" % (t+1, res))