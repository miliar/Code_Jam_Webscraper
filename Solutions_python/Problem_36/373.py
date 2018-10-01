import os


filein=open("c:\\codejam\\welcome\\C-large.in",'r')
fileout=open("c:\\codejam\\welcome\\C-large.out",'w')

N=int(filein.readline().replace('\n',''))
com='welcome to code jam'
for line in range(N):
    s=filein.readline().replace('\n','')
    b=[0   for   row   in   range(19)]
    for i in range(len(s)):
        for k in range(19):
            j=18-k
            if s[i]==com[j]:
                if j==0:
                    b[j]+=1
                    b[j]%=10000
                elif b[j-1]!=0:
                    b[j]+=b[j-1]
                    b[j]%=10000
    s=str(b[18])
    s='0'*(4-len(s))+s
    fileout.write("Case #"+str(line+1)+": "+s+'\n')
          
        
        
filein.close()
fileout.close()