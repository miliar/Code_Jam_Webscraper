f = open("c:/Users/Laszlo/Documents/Program/Python/CodeJam/2013/B-large.in")
out = open("c:/Users/Laszlo/Documents/Program/Python/CodeJam/2013/test2.out", "w+")

T = int(f.readline())

for i in xrange(T):
    n,m = tuple([int (x) for x in f.readline().split()])
    lawn=[]
    for j in xrange(n):
        lawn.append([int(x) for x in f.readline().split()])
    possible = "YES"
    for r in xrange(n):
        for c in xrange(m):
            row = max(lawn[r])
            column = max([ x[c] for x in lawn])
            if min(row,column)> lawn[r][c]:
                possible = "NO"
    out.write("Case #%d: %s\n"%(i+1,possible))
                
    
f.close()
out.close()
