def tidy(N):
    if N < 10:
        return True

    N = str(N)
    tidys =  True
    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            tidys  = False
    return tidys

def tidyNum(N):

    for i in range(N,0,-1):
        if tidy(i):
            return i


cases = eval(input())

for i in range(cases):
    N = eval(input())
    result = tidyNum(N)
    print("Case #" + str(i + 1) + ": " + str(result))