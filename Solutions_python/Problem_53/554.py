def readinputfile(inputdata):
    lines=inputdata.split('\n')
    i = int(lines[0])
    ret=[]
    for j in xrange(i):
        ret.append((int(lines[1+j].split(' ')[0]), int(lines[1+j].split(' ')[1])))
    return (i, ret)


def runcase(n, k):
    return (0 == ((k+1)%(2**n)))

def main():
    INPUT_FILE = 'c:\\Users\\hp\\Desktop\\A-large.in'
    d = open(INPUT_FILE,'r').read()
    a = readinputfile(d)
    for i in xrange(a[0]):
        n,k = a[1][i]
        b=runcase(n,k)
        if (b):
            b = 'ON'
        else:
            b = 'OFF'
                    
        print 'Case #%d: %s'%(i+1,b)

main()
    
    
