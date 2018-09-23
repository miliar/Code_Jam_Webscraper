from Queue import *

n = int(raw_input())

def get_split(n):
    if n % 2 != 0:
        return int((n)/2), int((n)/2)
    else:
        return int(n/2), int(n/2)-1


for i in xrange(n):
    total, people = [int(s) for s in raw_input().split(" ")]
    q = []
    least, maximum = 0,0
    q.append(total)
    for j in range(people):
        current = q[0]
        q = q[1:]
        maximum, least = get_split(current)
        q.append(maximum)
        q.append(least)
        q.sort(reverse=True)

    print "Case #{}: {} {}".format(i + 1, maximum, least)