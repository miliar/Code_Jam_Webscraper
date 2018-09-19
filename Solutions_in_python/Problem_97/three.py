def equals (a, b):
    return (a[0] == b[0] and a[1] == b[1]) or (a[0] == b[1] and a[1] == b[0])        

def rot(s):
    li = [s]
    for i in xrange(len(s)-1):
        li.append(li[-1][-1]+li[-1][0:-1])
    return li 

f = open("c.in")
n = f.readline()
def contains(sets, b):
    return any([equals(a,b) for a in sets])

for (lineNum, line) in enumerate(f):
    ranges = [int(i) for i in line.split()]
    nums = [repr(i) for i in range(ranges[0], ranges[1] + 1)]
    sets = []
    for snum in nums:
        for pm in rot(snum):
            if pm != snum and not contains(sets, (pm,snum)) and pm in nums:
                sets.append((pm,snum))
    print "Case #%d: %d" % (lineNum+1,len(sets))
        
    
    
