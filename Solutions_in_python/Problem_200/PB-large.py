def is_tidy(x):
    x = str(x)
    for i in range(1,len(x)):
        if x[i-1]>x[i]:
            return False
    return True

def sol(N):
    if is_tidy(N): return N
    return sol(N//10-1)*10+9

T = int(input())
for _ in range(1,T+1):
    print('Case #%d:'%_,sol(int(input())))
