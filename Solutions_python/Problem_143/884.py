f=open('B-small-attempt1.in','r')
fo=open('out.out','w+')
n=int(f.readline().rstrip())
a=[]	
z=0
count=[]


for z in range(n):
        a=f.readline().rstrip().split()
        count.append(0)
        for i in range(int(a[0])):
                for j in range(int(a[1])):
                        if((i & j) < int(a[2])):
                                count[z]+=1
                   
g=1
for t in count:
        fo.write("Case #"+str(g)+": "+str(t)+"\n")
        g+=1
f.close()
fo.close()
