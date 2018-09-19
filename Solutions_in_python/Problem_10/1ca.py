def solve(P, K, L, letters):
    #print P, K, L, letters
    if L > P * K:
        res = "Impossible"
    else:  
        letters.sort(reverse=True)
        sum = 0
        p = 1
        k = 1
        for l in letters:
            sum += l * p
            k += 1
            if k > K:
                k = 1
                p += 1
        res = "%d" % sum
    return res


#fname = "A.in"
#fname = "A-small-attempt0.in"
fname = "A-large.in"
fin = open(fname, "r")
fOutName = fname.split(".")[0] + ".out"
fout = open(fOutName, "w")
num = int(fin.readline().strip("\n"))
for i in xrange(1, num + 1):
    P, K, L = [int(x) for x in fin.readline().split()]
    letters = [int(x) for x in fin.readline().split()]
    str = "Case #%d: %s" % (i, solve(P, K, L, letters))
    print str
    fout.write(str + "\n") 
fin.close()
fout.close()
