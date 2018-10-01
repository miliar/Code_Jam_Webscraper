#minimum

if __name__ == '__main__':
    infile = open("input.in")
    outfile = open('output.out','w')
    case = int(infile.readline())
    for i in range(case):
        n = int(infile.readline())
        line1 = infile.readline().split()
        line2 = infile.readline().split()
        x = []
        y = []
        for item in line1:
            x.append(int(item))
        for item in line2:
            y.append(int(item))
        x.sort();#print x
        y.sort()
        y.reverse();#print y
        p = 0
        for j in xrange(n):
            p += x[j] * y[j]
        outfile.write('Case #%d: %d\n'%(i + 1,p))
    infile.close()
    outfile.close()
    
        
        
            
            
