"""Rotate"""

def rotate(k, n, g):
    colors = ['R','B']
##    i=n-1
##    while i>=0:
##        count = 0
##        j=n-1
##        while g[i][j] == '.':
##            j -= 1
##            count -= 1
##        if count==-n:
##            del g[i]
##        else:
##            
##            g[i] = '.'+g[i][:count]
##            g[i] += '.'
##        i -= 1
##    print g
    for i in range(n):
        g[i] = list(g[i])
        while '.' in g[i]:
            g[i].remove('.')
        g[i].append('.')
        g[i].insert(0,'.')
    g.append('.'*(n+2))
##    print g
    for i in range(len(g)):
        for j in range(-2,-len(g[i]),-1):
            if g[i][j]=='.':
                continue
            for m in range(len(colors)):
                if not colors:
                    return "Both"
                if m==1 and len(colors)<=1:
                    m=0
                
                if g[i][j] == colors[m]:
##                    print "processing g[%d][%d] = '%s'" % (i,j,colors[m])
                    joined = False
                    for u in range(1,k):
                        if g[i+u][j]!=colors[m]:
                            break
                        if u==k-1:
                            joined = True
                    if joined:
                        """got!!"""
                        del colors[m]
                        continue
                    
                    for u in range(1,k):
                        if g[i][j-u]!=colors[m]:
##                            print "testing g[%d][%d]='%s' != '%s'" % (i,j+u,g[i][j+u], colors[m])
                            break
                        if u==k-1:
                            joined = True
                    if joined:
                        """got!!"""
                        del colors[m]
                        continue

                    for u in range(1,k):
                        if g[i+u][j-u]!=colors[m]:
                            break
                        if u==k-1:
                            joined = True
                    if joined:
                        """got!!"""
                        del colors[m]
                        continue

                    for u in range(1,k):
                        if g[i+u][j+u]!=colors[m]:
                            break
                        if u==k-1:
                            joined = True
                    if joined:
                        """got!!"""
                        del colors[m]
                        continue
            """end for m"""
    if len(colors) == 0:
        return "Both"
    if len(colors) == 2:
        return "Neither"
    if colors[0] == 'R':
        return "Blue"
    else:
        return "Red"

##n = 4
##k = 4
####g = [['R','.','.','.'],
####     ['B','R','.','.'],
####     ['B','R','.','.'],
####     ['B','R','.','.']]
##g = ["R...",
##"BR..",
##"BR..",
##"BR.."]

##print rotate(k,n,g)
fp = open("A-large.in", 'r')
fout = open("A-large.out", 'w')
T = int(fp.readline())
for i in range(T):
    n,k = fp.readline().split()
    n = int(n)
    k = int(k)
    g = []
    for j in range(n):
        g.append( fp.readline().strip() )
    fout.write("Case #%d: %s\n" % (i+1, rotate(k,n,g) ))
fp.close()
fout.close()
