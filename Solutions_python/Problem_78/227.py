import math

TASK = 'A'
REQ  = 'L'

def strFile(str):
    if REQ == 'L':
        res = '-large'
    elif REQ == 'T':
        res = ''
    else:
        res = '-small-attempt' + REQ
    return 'c:\\jam\\' + TASK + res + '.' + str 

def f1(rr):
    r = int(rr)
    w = 100
    if r > 0:
        if math.floor(r/2.0) == r/2.0:
            r /= 2
            w /= 2 
        if math.floor(r/2.0) == r/2.0:
            r /= 2
            w /= 2 
        if math.floor(r/5.0) == r/5.0:
            r /= 5
            w /= 5 
        if math.floor(r/5.0) == r/5.0:
            r /= 5
            w /= 5 

    return [r, w]

def nod100(rr):
    r = int(rr)
    res = 1
    if r > 0:
        if math.floor(100/float(rr)) == 100.0/float(rr):
            res = int(rr)
        else:
            if math.floor(r/5.0) == r/5.0:
                res = 5
            else:
                if math.floor(r/2.0) == r/2.0:
                    res = 2
    return res
   
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def main():
    inFile = open(strFile('in'))

    T = int(inFile.readline())

    r = []
    for i in range(0, T):
        line = inFile.readline()

        m = line[:-1].split(' ')
        n = int(m[0])

        res = 'Possible'
        if int(m[2]) == 0:
            if int(m[1]) > 0:
                res = 'Broken'
        else:
            if int(m[2]) == 100:
                if int(m[1]) < 100:
                    res = 'Broken'
            else:
                z = 100 / gcd(100, int(m[1]))
                if n < z:
                    res = 'Broken'
            
        r.append(res)
        print res

    outFile = open(strFile('out'), 'w')
    print strFile('out')
    for i in range(0, T):
        outFile.write('Case #%d: %s\n' % ((i+1), r[i]))
    outFile.close


if __name__ == '__main__':
    main()

