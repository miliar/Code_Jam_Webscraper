import math

def getNextList(l):
    resultList = []
    for el in l:
        resultList.append(int(el / 2))
        if int(el) % 2 == 0:
            resultList.append(int(el / 2) - 1)
        else:
            resultList.append(int(el / 2))
    return resultList

fi = open('C-small-2-attempt0.in', 'r')
fo = open('outputC-small.txt', 'w')

T = int(fi.readline())

for t in range(T):

    lineTokens = fi.readline().split()
    N = int(lineTokens[0])
    K = int(lineTokens[1])
    
    waitingList = [N]
    k = K

    for q in range(int(math.log(N, 2) + 1)):
        waitingList = getNextList(waitingList)

        if k <= int(len(waitingList) / 2):
            
            break
        k -= int(len(waitingList) / 2)       
        waitingList = sorted(waitingList, reverse=True)

    rl = waitingList[(k - 1) * 2]
    rr = waitingList[(k - 1) * 2 + 1]

    print('Case #{0}: {1} {2}'.format(t+1, rl, rr))
    fo.write('Case #{0}: {1} {2}\n'.format(t+1, rl, rr))

fi.close()
fo.close()

