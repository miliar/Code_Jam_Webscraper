def solve(N):
    procN = N
    arrN = []
    while procN > 0:
        arrN.append(procN % 10)
        procN /= 10
    arrN = arrN[::-1]

    last_index = len(arrN)
    for i in range(len(arrN) + 1):
        for j in range(1, last_index):
            if arrN[j - 1] > arrN[j]:
                last_index = j
                arrN[j - 1] -= 1
                break
    
    for i in range(last_index, len(arrN)):
        arrN[i] = 9;

    res = 0
    for i in arrN:
        res = res * 10 + i

    return res

T = input()
for t in range(1, T + 1):
    N = input()
    print 'Case #%d: %d'%(t, solve(N))
