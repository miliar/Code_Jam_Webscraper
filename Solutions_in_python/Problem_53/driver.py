SET_NAME = 'A-large'

def solve_case(infile):
    (n,k) = map(int, infile.readline().split())
    return "ON" if (k+1) % 2**n == 0 else "OFF"

def main():
    """
    Standard main method for all google code jam problems
    """
    infile = open('%s.in'%(SET_NAME))
    outfile = open('%s.out'%(SET_NAME), 'w')
    num_cases = int(infile.readline())
    for i in xrange(num_cases):
        print 'Solving case #%d...'%(i+1)
        output = 'Case #%d: %s\n'%(i+1, solve_case(infile))
        print output
        outfile.write(output)
    outfile.close()
               
if __name__ == '__main__':
    main()