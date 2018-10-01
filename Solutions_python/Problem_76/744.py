#!/usr/bin python

def summe(l):
    ret = 0
    for x in l:
        ret ^= x
    return ret

def equal(l1, l2):
    #print "checking",l1,l2
    return summe(l1)==summe(l2)

def getSplits(liste):
    for x in product([True, False],repeat = len(liste)):
        l1 = [e for i,e in enumerate(liste) if x[i]]
        l2 = [e for i,e in enumerate(liste) if not x[i]]
        if len(l1) > 0 and len(l2) > 0 and len(l1) >= len(l2):
            yield([l1,l2])
 
''' from http://docs.python.org/library/itertools.html#itertools.product '''
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def main():
    path = "C-small-attempt0.in"
    f = open(path)

    C = f.readline()
    for case in range(int(C)):
        f.readline()
        line = f.readline()
        line = line.strip()
        linetokens = line.split(' ')
        linetokens = [int(x) for x in linetokens]

        res = -1
        for possible in getSplits(linetokens):
            if equal(possible[0], possible[1]):
                #print "equal"
                value = sum([x for x in possible[0]]) 
                if value > res:
                    res = value
        if res < 0:
            result = "NO"
        else:
            result = res

        print "Case #"+str(case+1)+": "+str(result)

if __name__ == "__main__":
        main()
