def first_decr(N):
    i = 1
    while i < len(N) and int(N[i]) >= int(N[i-1]):
        i += 1
    if i == len(N):
        return None
    else:
        return i

T = int(input())
for i in range(1,T+1):
    N = list(input())
    ind = first_decr(N)
    while ind != None:
        N[ind-1] = str(int(N[ind-1])-1)
        for j in range(ind,len(N)):
            N[j] = '9'
        ind = first_decr(N)
    first_non_zero = 0
    while N[first_non_zero] == '0':
        first_non_zero += 1
    N = N[first_non_zero:]
    print("Case #"+str(i)+": "+''.join(N))
