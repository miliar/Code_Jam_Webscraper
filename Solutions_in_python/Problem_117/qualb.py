fin = open("B-large.in", "r")
fout = open("largeB.out", "w")


def next():
    return fin.readline().strip()
    
    
    
    
for case in xrange(1, int(next()) + 1):
    fout.write("Case #" + str(case) + ": ")
    print case
    rows, columns = map(int, next().split(" "))

    target = []
    
    for i in xrange(0,rows):
        target += map(int, next().split(" ")) 
        
    rowmax = []
    colmax = []
    
    for i in xrange(0, rows):
        rowmax.append( max( target[columns * i: columns * (i + 1)] )  )
        
    for i in xrange(0, columns):
        colmax.append( max( target[i::columns]  )  )
        
    for i in xrange(0, rows * columns):
        if target[i] < rowmax[i // columns] and target[i] < colmax[i % columns]:
            fout.write("NO")
            break
    else:
        fout.write("YES")
    
    fout.write('\n')
fin.close()
fout.close()