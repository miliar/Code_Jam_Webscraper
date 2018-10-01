
f = open('B-large.in')
out = open('out.txt', 'w')

testNum = int(f.readline())

for i in range (testNum):
    (N, M) = (int(x) for x in f.readline().split())
    data = []
    for j in range (N):
        data.append([int(x) for x in f.readline().split()])
    # solve the problem
    rowmax = []
    colmax = []
    for row in data:
        rowmax.append(max(row))
    for k in range(M):
        l = []
        for row in data:
            l.append(row[k])
        colmax.append(max(l))

    #print (rowmax)
    #print (colmax)
    #print ('')

    locMinFound = False;

    for n in range(N):
        if locMinFound:
            break
        for m in range(M):
            if data[n][m] < rowmax[n] and data[n][m] < colmax[m]:
                locMinFound = True
                break
    
    if locMinFound:
        out.write('Case #{0}: NO\n'.format(i + 1))
    else:
        out.write('Case #{0}: YES\n'.format(i + 1)) 
           




    

