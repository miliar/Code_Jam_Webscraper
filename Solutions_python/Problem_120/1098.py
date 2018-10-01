import math
fout=open("bullseye-small-out.txt", "wb+")
f = open("bulley.in", "r+")
def large(N,r,k):
    N=N-1
    computed=(2*N*N)+(((2*r)-1)*N)
    if computed<k:
        return N
    large(N,r,k)
def outval(constant,value):
    k=constant*constant
    k=k+(8*value)
    k=math.sqrt(k)
    k=k-constant
    k=k/4
    #print k
    return k
#i = raw_input()
i=f.readline()

T=int(i)
temp=T
while T>0:
    #i=raw_input()
    i=f.readline()
    r=long(i.split(" ")[0])
    k=long(i.split(" ")[1])
    constant=(2*r-1)
    N=int(outval(constant,k))
    computed=(2*N*N)+(((2*r)-1)*N)
    if computed>k:
        N=large(N,r,k)
    #print "case #"+str(temp-T+1)+": "+str(N)
    fout.write("Case #"+str(temp-T+1)+": "+str(N))
    fout.write("\n")
    Case=False
    T=T-1
fout.close()
f.close()
print "over"
