import sys
if(len(sys.argv) > 1):
    f = open(sys.argv[1])
    fout = open('output.out', 'w')
    t = int(f.readline())
    for i in range(t):
        added = 0
        data = f.readline().split(' ')
        smax = int(data[0])
        s = 0
        for j in range(smax+1):
            a = int(data[1][j])
            s += a
            if(s < j+1):
                diff = j+1 - s
                added += diff
                s += diff
        fout.write('Case #' + str(i+1) + ': ' + str(added) + '\n')
    
