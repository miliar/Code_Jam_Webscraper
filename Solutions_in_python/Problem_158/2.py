import sys

sol = [ [[0 for i in range(4)] for j in range(4)] for k in range(4)]
sol[0][0] = [1,0,0,0]
sol[0][1] = [1,1,0,0]
sol[0][2] = [1,0,0,0]
sol[0][3] = [1,1,0,0]
sol[1][1] = [1,1,0,0]
sol[1][2] = [1,1,1,0]
sol[1][3] = [1,1,0,0]
sol[2][2] = [1,0,1,0]
sol[2][3] = [1,1,1,1]
sol[3][3] = [1,1,0,1]


#print sol
fi = sys.stdin
t = int(fi.readline())

names = [ "RICHARD","GABRIEL"]

for _t in range(t):
    	line = fi.readline().split()
    	x = int(line[0])
    	r = int(line[1])
    	c = int(line[2])
        c1 = c

        if (r > c):
            c = r
            r = c1
        #print "hel : " ,r,c,x,sol[r-1][c-1][x-1]
        print "Case #%d: %s" % (_t+1,names[sol[r-1][c-1][x-1]])		

