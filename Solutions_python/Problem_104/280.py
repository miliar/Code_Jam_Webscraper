#!/usr/bin/python2.7


from sys import argv, stdin, stdout

inf, ouf = stdin, stdout
cache = {}

def logger(case, output):
    ouf.write("Case #%d: %s\n" %(case, output))
    ouf.flush()


def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc


def xuniqueCombinations(items, n):
    if n == 0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
                

def eqsums(S):
    sums = {}
    found = False
    for i in xrange(len(S)):
        for s in tuple(xuniqueCombinations(S, i)):
            ssum = sum(s)
            p = sums.get(ssum)
            if p is None:
                sums[ssum] = s
            else:
                #print s
                #print p
                found = True
                break
        if found:
                break

    if found:
        return [s, p]
    else:
        return []


def main():
    T = int(inf.readline())
    for x, line in enumerate(inf.readlines(), 1):
        nline = [int(i) for i in line.split()]
        N = nline[0]
        S = nline[1:]
        ss = eqsums(S)
        ouf.write("Case #%d:\n" %(x, ))
        if not any(ss):
            ouf.write("Impossible\n")
        else:
            set1 = " ".join([str(i) for i in ss[0]])
            set2 = " ".join([str(i) for i in ss[1]])
            ouf.write("%s\n" %(set1, ))
            ouf.write("%s\n" %(set2, ))
        ouf.flush()


   

if __name__ == '__main__':
    #gen()
    main()
 
