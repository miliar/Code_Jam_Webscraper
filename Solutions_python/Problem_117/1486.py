import string

def solve(heights, N, M):
    return all( [ all([ c == max(row) or c == max([r[i] for r in heights]) for i,c in enumerate(row)]) for row in heights] )


def main():

    infile = open('a.in','r')
    outfile = open('a.out','w')

    T = int(string.strip(infile.readline()))    

    for k in xrange(T):
        print k
        N,M = map(int,string.strip(infile.readline()).split())
        heights = [ map(int, string.strip(infile.readline()).split()) for i in range(N)]
        if solve(heights, N, M):
            answer = 'YES'
        else:
            answer = 'NO'
        outfile.write('Case #%d: %s\n' % (k+1,answer))


if __name__ == '__main__':
    main()

