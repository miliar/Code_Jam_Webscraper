import sys
inputFile=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\a-small.in')
output=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\a-small.out',mode='w')
sys.stdin = inputFile
c = int(input())
for i in range(1,c+1):
    ab=[]
    n = int(input())
    for j in range(n):
        a,b =[int(k) for k in input().split()]
        ab.append((a,b))
    ans = 0    
    for j in range(n-1):
        for k in  range(j+1,n):
            order1 = ab[j][1]-ab[k][1]
            order2 = ab[j][0]-ab[k][0]            
            if(order1*order2<0):
                ans+=1           
    print('Case #{0}: {1}'.format(i,ans),file=output)
output.close()
inputFile.close()
