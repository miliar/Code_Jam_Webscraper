import sys
import math

def combin(n, k):
    return reduce(lambda a,b: a*(n-b)/(b+1), xrange(k), 1)



if __name__ == '__main__':
    ### PROGRAM CCCCCCCCCCCCC
    #openfile = open('A.in', 'r')

    #precompute
    M = 25
    subsets = []
    for j in range(M+1):
        subsets.append([0 for _ in range(M)])
    #for j in range(M+1):
    #    print subsets[j][1:]
    subsets[2][1] = 1
    for j in range(3, M+1):
        subsets[j][1] = 1
        subsets[j][2] = 1
        subsets[j][j-1] = 1

    for j in range(3, M+1):
        for s in range(3, j-1):
            for k in range(s-1):
                c = combin(j-s-1, k)
                subsets[j][s] += c*subsets[s][s-k-1]
    #for j in range(2, M+1):
    #    print subsets[j][1:]

    openfile = sys.stdin
    ET = int(openfile.readline()[:-1])
    for T in range(1, ET+1):
        # read test data
        n = int(openfile.readline()[:-1])
        num_sets = sum([subsets[n][s] for s in range(1, n)]) % 100003
        print 'Case #%s: %s' %(T, num_sets)
    openfile.close()
