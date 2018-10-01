#!/usr/bin/python
casenumber = int(raw_input())

for case in range(0, casenumber):
    Row,Column = [int(x) for x in raw_input().split(' ')]
    simulate = []
    initialSet = []
    emptySet = []
    children = []
    for r in range(Row):
        line = raw_input()
        simulate_r = []
        for c in range(Column):
            simulate_r.append(line[c])
        simulate.append(simulate_r)
    #print simulate

    #print 'round1'
    for x in range(Row):
        for y in range(Column):
            #print simulate[x][y]
            if simulate[x][y] == '?':
                closest = Column
                closestY = 0
                for col in range(Column):
                    if col!=y and simulate[x][col] != '?' and abs(col-y)<=closest:
                        closest = abs(col-y)
                        closestY = col
                simulate[x][y] = simulate[x][closestY]

    #print 'round2'
    for y in range(Column):
        for x in range(Row):
            #print simulate[x][y]
            if simulate[x][y] == '?':
                closest = Row
                closestX = 0
                for row in range(Row):
                    if row!=x and simulate[row][y] != '?' and abs(row-x)<closest:
                        closest = abs(row-x)
                        closestX = row
                simulate[x][y] = simulate[closestX][y]


    print 'Case #{}:'.format(case+1)
    for r in range(Row):
            print ''.join(simulate[r])



