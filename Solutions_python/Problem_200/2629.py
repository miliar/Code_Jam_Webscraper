

def tidy(N):
    a = ''

    for i in  range(len(N)-1):
        if N[i] > N[i+1]:
            a = N[:i] + str(int(N[i])-1) + '9'*len(N[i+1:])
            return int(tidy(a))



    return int(N)



T = int(input())

for i in range(1,T+1):
    N = str(input())
    print ("Case #{}: {}".format(i,tidy(N)))
