fout=open('C:\\Users\Tahsin\Desktop\CodejamCode\outB.txt','w')
fin=open('C:\\Users\Tahsin\Downloads\B-large.in','r')
tests=int(fin.readline().strip())

#tests=int(input())

for test in range(tests):
    
    #line=input().strip()
    
    line=fin.readline().strip()
    pre=line.split()
    N=int(pre[0])
    S=int(pre[1])
    p=int(pre[2])
    points=[0]*N
    count=0
    possible=0
    for i in range(N):
        points[i]=int(pre[i+3])
    
    if p==0:
        count=N 
    elif p==1:
        for point in points:
            if point >= 1:
                count+=1
    else:
        for point in points:
            if point >= (p*3-2):
                count+=1
        for point in points:
            if point >= (p*3-4) and point < (p*3-2):
                possible+=1
        count+=min(possible,S)
    
    fout.write("Case #{0}: {1}\n".format(test+1, count))
            
        
    
    
    
    