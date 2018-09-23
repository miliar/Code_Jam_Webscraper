T = int(raw_input().strip())
for i in range(T):
    N = raw_input().strip()
    n = len(N)
    arr = []
    for j in range(n):
        arr.append(int(N[j]))
    for j in range(1,n):
        if arr[-j] < arr[-j-1]:
            for k in range(1,j+1):
                arr[-k] = 9
            arr[-j-1] -= 1
    answer = ""
    if arr[0] > 0: answer += str(arr[0])
    for j in range(1,n):
        answer += str(arr[j])
            
    print "case #" + str(i+1) + ": " + answer
            
            
    