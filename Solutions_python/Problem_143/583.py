import numpy as np
infile = r'C:\Users\PRATIK\Downloads\B-small-attempt0.in'
outfile =r'C:\Users\PRATIK\Downloads\B-small-attempt0-sol.txt'
ip = open(infile, 'r')
op = open(outfile, 'w')
t=int(ip.readline().strip())
for i in range(t):
    print i
    a,b,k=map(np.int64, ip.readline().strip().split())
    kl=np.arange(k)
    c=0
    for j in np.arange(a):
        for k in np.arange(b):
            if j&k in kl:
                c+=1
    op.write('Case #'+str(i+1)+': '+str(c)+'\n')
op.close()
