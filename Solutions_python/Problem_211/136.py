input = open('task3.in','r')
output = open('output.txt','w+')
T = int(input.readline())

for t in range(T):
    points = []
    N, K = map(int, input.readline().split())
    U = float(input.readline())
    x = list(map(float, input.readline().split()))
    x = sorted(x)

    for i in range(N-1):
        print(x, U)
        raz = x[i+1] -x[i]
        if raz*(i+1) < U:
            for j in range(i+1):
                x[j] = x[i+1]
            U -= raz*(i+1)
        else:
            dod = U/(i+1)
            for j in range(i+1):
                x[j] = dod + x[j]
            U = 0
            break
    print(x)
    if U > 0:
        for i in range(N):
            x[i] += U/N
            if x[i] > 1:
                x[i] = 1
    print(x)
    prod = 1
    for i in range(N):
        prod *= x[i]
    output.write("Case #{}: {}\n".format(t + 1, prod))