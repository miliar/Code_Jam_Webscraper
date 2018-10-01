T = int(input())
for loopC in range(T):
    N = int(input())

    N = list(str(N))

    for x in range(len(N)-1,0,-1):
        if N[x-1] > N[x]:
            N[x-1] = str(int(N[x-1])-1)
            for y in range(len(N)-x):
                N[x+y] = '9'
        #print(x-1,x,N)

    result = ""
    for c in N:
        result = result+c

    print("Case #{}: {}".format(loopC+1,int(result)))
    

