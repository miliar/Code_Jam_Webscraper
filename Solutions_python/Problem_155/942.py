def solve():
    sm,inv=0,0
    for i in range(n):
        if  i<=sm:
            sm+=int(l[i])
        elif int(l[i])>0:
            inv+=i-sm
            sm+=i-sm+int(l[i])
    return inv

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=[x for x in fin.readline().strip().split(' ')]
    n=int(line[0])+1 ; l=line[1] 
    fout.write("Case #"+str(case)+": "+str(solve())+"\n")