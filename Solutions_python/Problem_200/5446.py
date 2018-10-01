t=int(input())
for i in range (1,t+1):
    for s in input().split():
        n = int(s)
        p = 0
        while p < (len(str(n))-1):
            numbers = list(str(n))
            if int(numbers[p])<=int(numbers[p+1]):
                p = p + 1
            else:
                n = n - 1
                p = 0
        print ("Case #{}: {}".format(i, n))
