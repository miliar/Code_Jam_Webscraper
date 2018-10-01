import time
import math

# Found a mistake after my little submission.  The length being used in the inner loop
# should be the length of n and not of bigA.

debug = False

tStart = time.time()

fname = "C-large"
#fname = "test2"

fin = open(fname+".in","r")
flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")

numcases = int(flines[0])

decades = [1,10,10**2,10**3,10**4,10**5,10**6,10**7]

for icase in range(1,numcases+1):
    rawline = flines[icase].split()
    bigA = int(rawline[0])
    bigB = int(rawline[1])
    #print "A=%d, B=%d" % (bigA,bigB)

    nums = range(bigA,bigB+1)
    groups = [[]]
    for x in range(len(decades)-2):
        groups.append([])
    # stick the numbers into their groups
    for i in nums:
        for x in range(len(decades)-1):
            if i < decades[x+1]:
                groups[x].append(i)  # not fast, but good enough for now (I hope)
                break
        # could instead do the following but it isn't faster
        # groups[int(math.floor(math.log10(i)))].append(i)
       
    results = dict()
    for g in range(len(groups)):
        # Process one group
        for split in range(0,g+1):
            mfilt = 10**split
            mbase = 10**(g+1-split)
            for n in groups[g]:
                m = (n % mfilt) * mbase + (n / mfilt)
                if n < m and m <= bigB:
                    if (n,m) not in results:
                        results[(n,m)] = True
                
  
    outstr = "Case #%d: %d" % (icase,len(results))
    print outstr
    fout.write("%s\n" % (outstr))
    print "run time = %s" % (str((time.time() - tStart)))


fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))
