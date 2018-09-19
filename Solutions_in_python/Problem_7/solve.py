ifile=file("A-small-attempt1.in","r")
ofile=file("output.txt","w")

cases=int(ifile.readline())

def GetTrees(n, A, B, C, D, x0, y0, M):
    trees=[]
    X = x0
    Y = y0
    trees.append([X, Y])
    for i in range(n-1):
      X = (A * X + B) % M
      Y = (C * Y + D) % M
      trees.append([X, Y])

    print trees
    return trees
    
def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc                

for c in range(cases):
    data=ifile.readline().split()

    n = int(data[0])
    A = int(data[1])
    B = int(data[2])
    C = int(data[3])
    D = int(data[4])
    x0 = int(data[5])
    y0 = int(data[6])
    M = int(data[7])

    trees=GetTrees(n, A, B, C, D, x0, y0, M)

    ct=0
    for triangle in xuniqueCombinations(trees, 3):
        
        #calculate triangle centre
        x1=triangle[0][0]
        x2=triangle[1][0]
        x3=triangle[2][0]

        y1=triangle[0][1]
        y2=triangle[1][1]
        y3=triangle[2][1]

        xm=(x1+x2+x3)/3.0
        ym=(y1+y2+y3)/3.0

        #print "tri", triangle, "center", xm, ym

        if xm==int(xm) and ym==int(ym):
            #print "bingo", triangle
            ct=ct+1

    print >> ofile,"Case #%i: %i" % (c+1,ct)

ifile.close()
ofile.close()

print "########FIM#########"

