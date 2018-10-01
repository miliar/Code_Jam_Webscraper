import heapq

fi=open('ex3.in')
fo=open('ex3.out','w')
nCases=int(fi.readline())
for case in range(1,nCases+1):
    n,k=[int(tok) for tok in fi.readline().split()]
    hq=[-n]
    for i in range(k-1):
        topelt=-heapq.heappop(hq)
        if topelt%2:
            heapq.heappush(hq,-(topelt/2))
            heapq.heappush(hq,-(topelt/2))
        else:
            heapq.heappush(hq,-(topelt/2))
            heapq.heappush(hq,-(topelt/2-1))
    topelt=-heapq.heappop(hq)
    if topelt%2:
        fo.write('Case #%s: %s %s\n' % (case,topelt/2,topelt/2))
    else:
        fo.write('Case #%s: %s %s\n' % (case,topelt/2,topelt/2-1))

fi.close()
fo.close()
