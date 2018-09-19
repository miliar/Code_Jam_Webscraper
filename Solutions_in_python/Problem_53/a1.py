import math
fin = open('./A-large.in')
t = int(fin.readline())

fout = open('./A-large.out','w')
print "Start"
for i in xrange(1,t+1):
    n,k = [int(x) for x in fin.readline().split()]
    if (k+1) % math.pow(2,n) == 0:
        fout.write("Case #{0}: ON\n".format(i))
    else:
        fout.write("Case #{0}: OFF\n".format(i))
print "Done."