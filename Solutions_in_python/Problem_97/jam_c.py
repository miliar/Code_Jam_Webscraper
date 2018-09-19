import math

def rr(s, i):
    return  s[-i:] + s[:-i]

def main():
    inFile = open('c:/jam/2012/C-small-attempt0.in')
    
    c = int(inFile.readline())
    print c

    r = []
    
    for i in range(0, c):
        line = inFile.readline()
        [n, m] = line.split(' ')
        [n, m] = [int(n), int(m)]

        #res = []
        res = {}

        for j in range(n, m+1):
            z0 = str(j)
            for k in range(1, len(z0)):
                z1 = int(rr(z0, k))
                #print '%d - %d' % (j, z1)
                
                if z1 > j:
                    if z1 <= m:
                        #res.append(j)

                        #res[j] = z1
                        #res[z1] = j

                        res[str(j) + str(z1)] = ''
                                
        r.append(len(res))
        #print res

    outFile = open('c:/jam/2012/C.out', 'w')
    for i in range(0, c):
        outFile.write('Case #%d: %d\n' % ((i+1), r[i]))
        print r[i]
    outFile.close

if __name__ == '__main__':
    main()

