def getAndResult(ba, bb):
    new_str = ''
    for i in xrange(len(ba)):
        if ba[i] == '0' and bb[i] == '0':
           new_str = new_str + '0'
        elif ba[i] == '0' and bb[i] == '1':
           new_str = new_str + '0'
        if ba[i] == '1' and bb[i] == '0':
           new_str = new_str + '0'
        if ba[i] == '1' and bb[i] == '1':
           new_str = new_str + '1'
    return new_str

def getDecimal(numstr):
    total = 0
    numstr= numstr[::-1]
    for z in xrange(len(numstr)):
        if numstr[z] == '1':
            total = total + 2 ** z
    return total

def getPossibilities(a, b, k):
    count = 0
    klist = range(k)
    for x in xrange(a):
        for y in xrange(b):
            bin_a = bin(x)[2:]
            bin_b = bin(y)[2:]
            if len(bin_a) < len(bin_b):
                bin_a = '0' * (len(bin_b) - len(bin_a)) + bin_a
            elif len(bin_b) < len(bin_a):
                bin_b = '0' * (len(bin_a) - len(bin_b)) + bin_b
            res = getAndResult(bin_a, bin_b)
            dec = getDecimal(res)
            if dec in klist:
                count += 1
    return count

with open('B-small-attempt0.in', 'r') as fp:
    for tc in xrange(int(fp.readline())):
        A, B, K = [int(i) for i in fp.readline().strip('\n').split()]
        print "Case #%d: %d" % (tc+1, getPossibilities(A, B, K))
