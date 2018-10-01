
def mkDir(dTree, dirs):
    count = 0
    curDir = dTree['root']
    for d in dirs:
        if d not in curDir:
            count += 1
            curDir[d] = {}
        curDir = curDir[d]
    
    return count



ifile = open("A-large.in", 'r')
ofile = open("gcj-r-1Bb.txt", 'w')

T = int(ifile.readline())

for c in range(T):
    sline = ifile.readline().split()
    N = int(sline[0])
    M = int(sline[1])
    
    eP = []
    for l in range(N):
        line = ifile.readline().strip('\n')
        eP.append(line)
        
    wP = []
    for r in range(M):
        line = ifile.readline().strip('\n')
        wP.append(line)
    
    seen = {'root': {}}
    for p in eP:
        dirs = p.split('/')
        dirs.remove('')
        mkDir(seen, dirs)
    
    result = 0
    for cp in wP:
        cdirs = cp.split('/')
        cdirs.remove('')
        result += mkDir(seen, cdirs)
    
    ofile.write("Case #%d: %d\n" % (c+1, result))
                
