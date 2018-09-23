import math
import numpy as np
#dederlein
def solve(n):


    sol = []
    for i in range(R):
        s = n[i][0]
        for j in range(C):
            if s[j] != '?':
                for k in range(C):
                    if s[k] == '?':
                        s = s[:k] + s[j] + s[k+1:]
                        if k+1<=C-1 and s[k+1] == '?':
                            s = s[:k+1] + s[j] + s[k+2:]
                    elif s[k] != '?' and k>j:
                        break
        sol.append(s)

    y = 1
    while y==1:
        sol2 = []
        for i in range(R):
            if sol[i][0] == '?' and i>=1:
                sol2.append(sol[i-1])
            else:
                sol2.append(sol[i])
        sol = sol2
        y = 0
        for q in range(R-1):
            if sol[q][0] != '?' and sol[q+1][0] == '?':
                y = 1
                break


    x = 1
    while x == 1:
        sol3 = []
        for q in range(R):
            i = R-q-1
            if sol2[i][0] == '?' and i<R-1:
                sol3.append(sol2[i+1])
            elif sol2[i][0] != '?':
                sol3.append(sol2[i])
        sol2 = sol3[::-1]
        x = 0
        for q in range(R):
            if sol2[q][0] == '?':
                x = 1
                break



    sol4 = sol3[::-1]

    return 2,sol4






IN = open('Input.txt', 'r')
OUT = open('Output.txt', 'w')

T = int(IN.readline())

for line in range(T):
    # Instanz mit mehreren Zeilen
    yes = 1
    if yes == 0:
        #sizen = int(IN.readline())
        n = list(map(str, IN.readline().split()))
    else:
        T0 = list(map(int, IN.readline().split()))
        R = T0[0]
        C = T0[1]
        #n = list(map(int, IN.readline().split()))
        n = []
        for i in range(T0[0]):
            n.append(list(IN.readline().split()))

    #print(solve(n)[1])
    if solve(n)[0] == 1:
        answer = solve(n)[1]# ' '.join(map(str,solve(n)[1]))
        OUT.write('Case #{}: {}\n'.format(line + 1, answer))
    else:
        OUT.write('Case #{}:\n'.format(line + 1))
        for i in range(len(solve(n)[1])):
            answer = solve(n)#' '.join(map(str,solve(n)[1][i]))
            a = answer[1]
            OUT.write('{}\n'.format(a[i]))
    if yes == 1:
        line -= T0[0]
IN.close()
OUT.close()