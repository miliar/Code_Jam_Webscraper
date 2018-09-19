import sys

def minimum(filename):
    f = open(filename,'rb')
    line = f.readline()
    T = int(line.rstrip()) # T is the number of test cases
    results = []
    for i in range(T):
        line = f.readline()
        n = int(line.rstrip()) # n is the number of vectorss
        line = f.readline()
        v1 = [int(a) for a in (line.rstrip().split(' '))] # vectors 1
        line = f.readline()
        v2 = [int(a) for a in (line.rstrip().split(' '))] # vectors 2
        v1.sort()
        v2.sort()
        v2.reverse()
        result = 0
        for j in range(n):
            result += v1[j]*v2[j]
        results.append(result)
        
    k = 1
    for result in results:
        print 'Case #'+ str(k)+': '+str(result)
        k+=1
    f.close()

if __name__ == '__main__':
    minimum(sys.argv[1])
