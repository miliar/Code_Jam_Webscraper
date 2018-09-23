from math import ceil

def train(n, ticks):
    d = {}
    roller = []
    for i in range(n):
        roller.append(0)
    for i in range(len(ticks)):
        if ticks[i][1] in d:
            d[ticks[i][1]] += 1
        else:
            d[ticks[i][1]] = 1
        roller[(ticks[i][0]-1)] += 1

    maxtick = max(d.iteritems(), key = lambda x: x[1])
    maxtick = maxtick[1]

    maxcar = maxtick
    changes = 0

    totticks = 0
    for i in range(len(roller)):
        totticks += roller[i]
        submaxcar = int(ceil(totticks/float(i+1)))
        maxcar = max(submaxcar, maxcar)
        changes += max(roller[i]-maxcar, 0)

    return maxcar, changes


    



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    n, c, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    ticks = [[int(s) for s in raw_input().split(" ")] for line in range(m)]
    a = train(n, ticks)
    print "Case #{}: {} {}".format(i, a[0], a[1])