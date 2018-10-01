import sys
sys.setrecursionlimit(100000)

def CookieClick(a,c,f,x):
    if c/a+x/(a+f) < x/a:
        return c/a + CookieClick(a+f,c,f,x)
    else:
        return x/a

f1=open('C:/Python27/GCLqualsmallB', 'w+')

linelist = []
for line in open('C:\Users\User\Downloads\B-small-attempt0.in'):
    linelist.append(line.rstrip('\n'));

testnum = int(linelist[0]);

for i in xrange(1,testnum+1):
    inlist = linelist[i].split()
    c = float(inlist[0])
    f=float(inlist[1])
    x=float(inlist[2])
    f1.write("Case #"+str(i)+": "+str(CookieClick(2.0,c,f,x))+"\n")

f1.close()
