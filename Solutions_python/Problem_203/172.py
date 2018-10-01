IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

NUM_TESTS = int(IN.readline())

for test in xrange(NUM_TESTS):

    cake = []
    R, C = map(int,IN.readline().split())
    for _ in xrange(R):
        cake.append(IN.readline().strip())
    
    firstRow = '?' * C
    lastRow = '?' * C
    for i, row in enumerate(cake):
        newRow = ''
        first = '?'
        last = '?'
        for c in row:
            if c != '?':
                last = c
                if first == '?':
                    first = c
            newRow += last
        newRow = newRow.replace('?', first)
        cake[i] = newRow
        
        if newRow[0] != '?':
            lastRow = newRow
            if firstRow[0] == '?':
                firstRow = newRow
        else:
            cake[i] = lastRow
    i = 0
    while cake[i][0] == '?':
        cake[i] = firstRow
        i += 1
    
    
    OUT.write('Case #{}:\n'.format(test+1))
    print test+1
    
    for row in cake:
        OUT.write('{}\n'.format(row))
        print row

IN.close()
OUT.close()
