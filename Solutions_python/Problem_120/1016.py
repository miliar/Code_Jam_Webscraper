import math
def num():
    global n,r,t
    return int((math.sqrt(8*t+(2*r-1)**2)-2*r+1)/4)
global n,r,t
infile=open("A-small-attempt0.in",'r')
outfile=open("Bullseye",'w')
lines=infile.readlines()
infile.close()
n=int(lines[0][:-1])
for s in xrange(n):
    r,t=[int(i) for i in lines[s+1][:-1].strip().split()]
    outfile.write("Case #"+str(s+1)+": "+str(num())+"\n")
    #print "Case #"+str(s+1)+": "+str(num())
outfile.close()
