import sys
from collections import deque
f = open(sys.argv[1])

numItems = int(f.readline(),10)
current = 1
while current <= numItems:
    li = f.readline().split()
    R = int(li[0],10)
    k = int(li[1],10)
    N = int(li[2],10)
    groups  = deque([int(items) for items in f.readline().split()])
    cash = 0
    while R > 0:
        numPeople = 0
        count = 0;
        while count < len(groups):
            curr = groups.popleft()
            if numPeople + curr > k:
                groups.appendleft(curr)
                break
            else:
                groups.append(curr)
                count += 1
                numPeople += curr
                cash += curr
        R -= 1
    print "Case #%d: %d" % (current, cash)
    current += 1
