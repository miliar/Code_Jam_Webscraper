def lett(x):
    return chr(ord(x)+1)


def flowdir(y,x,matrix):
#    print 'flow dir start',y,x
    a,b = y,x    
    if (y-1>= 0) and (matrix[y-1][x] < matrix[a][b]):
        a,b =y-1,x
    if (x-1>= 0) and (matrix[y][x-1] < matrix[a][b]):
        a,b =y,x-1,
    if (x+1 < len(matrix[y])) and (matrix[y][x+1] < matrix[a][b]):
        a,b =y,x+1
    if (y+1 < len(matrix))  and (matrix[y+1][x] < matrix[a][b]):
        a,b =y+1,x
#    print 'flow dir end',a,b
    return a,b
        

    
def flow(y,x,matrix,res,label):
    if res[y][x]: return res[y][x]
    a,b = flowdir(y,x,matrix)
    if [a,b] == [y,x]:
        res[y][x] = label
        return label
    label = flow(a,b,matrix,res,label)
    res[y][x] = label
    return label        

f = open('test_large.in')
T = int(f.readline().strip())

for c in xrange(T):
    (H,W) = map(int,f.readline().split())
    matrix = [map(int,f.readline().split()) for _ in xrange(H)]
    res = [[False for _ in xrange(W)] for _2 in xrange(H)]
    label = 'a'
    for y in xrange(H):
        for x in xrange(W):
            if not res[y][x]:
                tmp = flow(y,x,matrix,res,label)
                if tmp is label:
                    label = lett(label)
    print 'Case #%d:'%(c+1)
    for x in res:
        print ' '.join(x)
    
                
                
                
        
