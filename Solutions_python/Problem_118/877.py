import time

t = time.clock()

def pal(v):
    s = str(v)
    for i in range(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True
vals = []
n = 10**14
v = 1
sq = 0
while sq <= n:
    if pal(v):
        sq = v ** 2
        if pal(sq):
            vals.append(sq)
    v += 1
#print vals

f = open("ProblemC-Large1.txt")
f.readline()

outFile = open("ProblemC-Out.txt",'w')
c = 0
while True:
    c+=1
    counts = f.readline()[:-1]
    if len(counts) == 0:
        break
    countsP = counts.split(' ')
    a = int(countsP[0])
    b = int(countsP[1])
    message = str(len([x for x in vals if a<= x <= b]))
    outFile.write("Case #{0}: {1}\n".format(c, message))
    print "Case #{0}: {1}".format(c, message)
    
print time.clock() - t
f.close()
outFile.close()

