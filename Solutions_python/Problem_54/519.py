# -*- coding: latin-1 -*- 

# o(n*logn)
def gcd(a, b):
    #print "gcd(" + str(a) + ", " + str(b) + ")"
    if (a % b) == 0:
        return b
    return gcd(b, a % b)

infile = open("a.in", "r")
outfile = open("a.out", "w")

C = int(infile.readline())

for j in range(C):
    tmp = (infile.readline()).split()
    
    N = int(tmp[0])
    t = tmp[1:]
    for i in range(len(t)):
        t[i] = int(t[i])
    
    # sort the list O(n*logn) so the smallest factor can be found
    # in O(n) time.
    t.sort()
    
    # find the smallest difference
    T = t[len(t)-1]-t[0]
    for i in range(len(t)-1):
        diff = t[i+1]-t[i]
        if diff == 0: continue
        T = min(T, t[i+1]-t[i])

    for i in range(len(t)-1):
        if t[i+1] == t[i]: continue
        syt = gcd(t[i+1] - t[i], T)
        if syt <> T:
            T = syt
    
    
    y = (int(t[0]/T)+1)*T-t[0]
    y = y % T
    
    #print str(T) + " ja " + str(y)
    outfile.write("Case #" + str(j+1) + ": " + str(y) + "\n")

outfile.close()
infile.close()



