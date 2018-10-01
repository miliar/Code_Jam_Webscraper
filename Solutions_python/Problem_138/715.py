import sys
import collections
line = sys.stdin.readline()
numTests = int(line)
for test in xrange(1, numTests+1):
    numBlocks = int(sys.stdin.readline())

    naiomi = sys.stdin.readline().split(' ')
    naiomi = [float(item) for item in naiomi]

    ken = sys.stdin.readline().split(' ')
    ken = [float(item) for item in ken]

    naiomi.sort()
    ken.sort()

    naiomiQ = collections.deque()
    kenQ = collections.deque()

    for item in naiomi:
        naiomiQ.append(item)

    for item in ken:
        kenQ.append(item)

    naiomiWarScore = 0
    while(naiomiQ):
        kenWeight  = kenQ.pop()
        naiomiWeight = naiomiQ.pop()
        if(naiomiWeight > kenWeight):
            naiomiWarScore += 1
            kenQ.append(kenWeight)
            kenQ.popleft()

    naiomiQ = collections.deque()
    kenQ = collections.deque()

    for item in naiomi:
        naiomiQ.append(item)

    for item in ken:
        kenQ.append(item)

    naiomiDeceitfulWarScore = 0
    while(naiomiQ):
        kenWeight  = kenQ.popleft()
        naiomiWeight = naiomiQ.popleft()
        if (naiomiWeight > kenWeight):
            naiomiDeceitfulWarScore += 1
        else:
            kenQ.appendleft(kenWeight)
            kenQ.pop()
            
    print 'Case #%d: %d %d' %(test, naiomiDeceitfulWarScore, naiomiWarScore)
