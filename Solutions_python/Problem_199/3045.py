
'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())

def number_flips(pstr,k):
    pbinrep = int(p.replace('-','0').replace('+','1'),2)
    np = len(p)

    count = 0
    # iterate and xor flipper if first bit isn't 1
    flipper = int(('1' * k) + ('0' * (np - k)),2)
    checker = int('1' + ('0' * (np-1)),2)
    for i in xrange(np-k+1):
        if not pbinrep & checker:
            pbinrep = pbinrep ^ flipper
            count = count + 1
        flipper = flipper >> 1
        checker = checker >> 1

    target = int('1' * np,2)
    if pbinrep == target:
        return count
    else:
        return None

for i in xrange(trials):
    p,k = infile.readline().split()


    nflips = number_flips(p,int(k))
    if nflips is None:
        answer = 'IMPOSSIBLE'
    else:
        answer = str(nflips)
    s = "Case #%d: %s\n" % (i+1,answer)
    outfile.write(s)
    print s
    
infile.close()
outfile.close()
