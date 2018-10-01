import sys, math

def handle(infile, outfile):
    n, A, B, C, D, x0, y0, M = [int(x) for x in infile.readline().split()]
    
    coords = [(0, 0)] * n
    x, y = x0, y0
    coords[0] = (x, y)
    for i in range(1, n):
        x = (A * x + B) % M
        y = (C * y + D) % M
        coords[i] = (x, y)
        
    tcount = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                xc = (coords[i][0] + coords[j][0] + coords[k][0]) / 3.0
                yc = (coords[i][1] + coords[j][1] + coords[k][1]) / 3.0
                #print '%d, %d, %d = ' % (i, j, k), xc, yc
                if xc == int(xc) and yc == int(yc): tcount += 1
    
    outfile.write(' %d' % tcount)

if len(sys.argv) != 2: exit()
infile = file(sys.argv[1], 'r')
outfile = file(sys.argv[1] + '.out', 'w')

count = int(infile.readline())
for i in range(count):
    print 'Case #%d' % (i + 1)
    outfile.write('Case #%d:' % (i + 1))
    result = handle(infile, outfile)
    outfile.write('\n')
