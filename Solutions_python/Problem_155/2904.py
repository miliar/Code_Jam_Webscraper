from __future__ import print_function
import sys




x=[]

rfile = open(sys.argv[1],'r')
lines = rfile.readlines()
rfile.close()

wfile = open(sys.argv[2],'w')



#number of test cases
for t in range(1,int(lines[0])+1):
    temp = lines[t].split()
    x=list(map(int, list(temp[1])))
    add=[0 for x in range(len(x))]
    y= [0 for x in range(len(x))]
    for s in range(0,len(x)):
        y[s] = y[s-1] + x[s-1]+ add[s-1] if s>0 else 0
        add[s]=0 if (s- y[s]) <=0 else s - y[s]

    print("Case #",t,": ",sum(add), sep='',file=wfile)


wfile.close()
