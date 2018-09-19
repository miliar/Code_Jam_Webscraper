#from time import clock
#print clock()

outputlist = []

def cycles(s):
    t = s
    for i in range(len(s)-1):
        t = t[1:] + t[:1]
        yield t

for i, testcase in enumerate(
                 open('C-large.in', 'r').read().splitlines()[1:]
                            ):
    strA, strB = testcase.split()
    A, B = int(strA), int(strB)
    
    ctr = 0
    
    for j in range(A, B+1):
        for c in set(cycles(str(j))):
            if j < int(c) <= B:
                ctr += 1
    
    outputlist.append('Case #%i: %i' % (i+1, ctr))
    print i

outputfile = open('RecycledNumbersOutputLarge.txt', 'w')
outputfile.write( '\n'.join(outputlist) )

#print clock()