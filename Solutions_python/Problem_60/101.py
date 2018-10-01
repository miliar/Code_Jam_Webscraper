import math,sys
fin = open('B-large.in','r')
sys.stdout = open('B-large.out','w')
    
C = int(fin.readline())
for c in range(1,C+1):
    N,K,B,T = [int(q) for q in fin.readline().split(' ')]
    x = [int(q) for q in fin.readline().split(' ')]
    v = [int(q) for q in fin.readline().split(' ')]
    time = [(B-x[i])/v[i] for i in range(0,N)]
    k = 0
    count = 0
    for i in range(N-1,-1,-1):
        j = i
        while j > -1 and time[j] > T: j-=1
        if j == -1: break
        if not j == i:
            temp = time[j]
            del time[j]
            time.insert(i,temp)
            count += i-j
        k+=1
        if k == K: break
    if k == K: print('Case #%d: %d' % (c,count))
    else: print('Case #%d: IMPOSSIBLE' % c)
fin.close()
