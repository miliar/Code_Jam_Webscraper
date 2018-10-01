
def solve(a,b,k):
    count=0
    for i in range(a):
        for j in range(b):
            if i&j <k:
                count+=1
    return count

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    a,b,k=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(a,b,k))+"\n")