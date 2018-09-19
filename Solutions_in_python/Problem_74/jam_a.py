import math

def main():
    inFile = open('c:\jam\A-large.in')

    c = int(inFile.readline())
    print c

    r = []

    for i in range(0, c):
        line = inFile.readline()
        m = line[:-1].split(' ')

        k = int(m[0])
        b = 0
        o = 0
        bp = 1
        op = 1
        step = 0
        
        for j in range(0, k):
            z = int(m[2+j*2])
            if m[1+j*2] == 'O':
                t = abs(z-op)
                if (o+t) < step:
                    o = step
                else:
                    o += t
                o += 1
                step = o
                op = z
            else:
                t = abs(z-bp)
                if (b+t) < step:
                    b = step
                else:
                    b += t
                b += 1
                step = b
                bp = z

        r.append(step)

    outFile = open('c:\jam\A-large.out', 'w')
    for i in range(0, c):
        outFile.write('Case #%d: %d\n' % ((i+1), r[i]))
    outFile.close


if __name__ == '__main__':
    main()

