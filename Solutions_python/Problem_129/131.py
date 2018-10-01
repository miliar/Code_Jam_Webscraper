import bisect

fn = 'A-small-attempt2'
input = open(fn+'.in','r')
output = open(fn+'.out', 'w')

def solve(case):
    N, M = [int(n) for n in input.readline().split()]
    Psg = []
    for i in range(M):
        o, e, p = [int(n) for n in input.readline().split()]
        Psg.append([o,e,p])

    #Calc normal cost
    normCost = 0
    for i in range(M):
        d = Psg[i][1] - Psg[i][0]
        normCost += Psg[i][2] * (d * N - int(d*(d-1)/2))

    Psg.sort(key=lambda x:x[0])

    #Look for longest stretch greedily
    minCost = 0
    while len(Psg) > 0:
        s = Psg[0][0]
        e = Psg[0][1]
        n = Psg[0][2]

        swap = False
        for i in range(1, len(Psg)):
            curS = Psg[i][0]
            curE = Psg[i][1]
            curN = Psg[i][2]
            if curS > e: #Too far, cannot reach
                break
            elif curE > e: #Swap, and continue
                numSwap = min(n, curN)
                remain = n - numSwap
                curRemain = curN - numSwap
                if curRemain == 0:
                    Psg.pop(i)
                else:
                    Psg[i][2] = curRemain
                if remain == 0:
                    Psg.pop(0)
                else:
                    Psg[0][2] = remain

                #Create new class of passengers of starters and swappers
                Psg.append([curS, e, numSwap])
                Psg.sort(key=lambda x:x[0])
                Psg.insert(0,[s,curE,numSwap])
                swap = True
                break


        if not swap:
            #First set of passengers now are as far as they can go
            s = Psg[0][0]
            e = Psg[0][1]
            n = Psg[0][2]
            d = e - s
            minCost += n * (d * N - int(d*(d-1)/2))
            Psg.pop(0)



    print("Case #{0}: {1}".format(case, (normCost-minCost)%1000002013), file=output)
    print("Case #{0}: {1}".format(case, (normCost-minCost)%1000002013))


import time
start = time.clock()

T = int(input.readline())
for i in range(1,T+1):
    solve(i)

print("{0} milliseconds".format((time.clock() - start) * 1000))
