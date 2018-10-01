f=open('B-large.in')
out=open('output.txt','w')
T=int(f.readline())
for i in range(T):
    out.write('Case #'+str(i+1)+': ')
    temp=f.readline().split()
    temp=temp[0]
    n=len(temp)
    #out.write(str(n) + '\n')
    if n==1:
        out.write(temp[0]+'\n')
        continue
    N = [0 for j in range(n)]
    for j in range(n):
        N[j]=int(temp[j])
    head=0
    while head<(n-1):
        if N[head]>N[head+1]:
            N[head]=N[head]-1
            N[(head+1):]=[9 for j in range(n-head-1)]
            if head!=0:
                head=head-1
            #for k in range(n):
            #    if not((N[k]==0)&(k==0)):
            #        out.write(str(N[k]))
            #out.write('\n')
        else:
            head=head+1
    for k in range(n):
        if not ((N[k] == 0) & (k == 0)):
            out.write(str(N[k]))
    out.write('\n')

f.close()
out.close()
