def xor(x,y):
    return x^y

T = input()
for caseID in range(1,T+1):
    N = input()
    numList = sorted(map(int,raw_input().split()))
    check = reduce(xor,numList,0)
    if check != 0:
        print "Case #%d: NO" % (caseID)
    else:
        res = sum(numList) - numList[0]
        print "Case #%d: %d" % (caseID,res)
