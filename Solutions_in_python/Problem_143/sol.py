import numpy

f = [line.rstrip() for line in open('/Users/roshil/Desktop/B-small-attempt0.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1, testcases+1):
    lis = [int(a) for a in f[line].split()]
    line += 1
    a,b,k = lis[0], lis[1], lis[2]
    n = 0
    for j in range(a):
        for l in range(b):
            if j&l < k:
                #print j,l
                n += 1
    print n
    out.write("case #"+str(i)+": "+ str(n) + "\n")
print n
out.close()
    
        