def All(A,B,K):
    Winning = set(range(K))
    Count = 0
    for a in range(A):
        for b in range(B):
            if a&b in Winning:
                Count += 1
    return Count

J=open('d.out','w')
with open('B-small-attempt1.in','r') as Reader:
    Total=Reader.read().split('\n')
    size = int(Total[0])
    Total=Total[1::]
    c=1
    for i in Total:
        a,b,k=map(int,i.split(' '))
        Line = 'Case #'+str(c)+': '+str(All(a,b,k))
        print Line
        J.write(Line)
        c+=1
J.close()
        
        
        
            
