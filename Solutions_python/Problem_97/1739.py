from collections import deque
from collections import defaultdict
l=deque()
m=deque()
fin = open("input.txt",'r')
fout= open("output1.txt",'w')
t=int(fin.readline())
for testcase in range(1,t+1):
    d=defaultdict(list)
    count=0
    a,b=map(int,fin.readline().split(" "))
    for i in range(a,b):
        for j in range(a+1,b+1):
            if(i!=j):
                l=deque(str(i))
                m=deque(str(j))
                if len(l)==len(m):
                    for length in range(1,len(l)):
                        l.rotate(1)
                        if((l==m) and ((j not in d[i])and(i not in d[j]))):
                            d[i].append(j)
                            count+=1        
    print("Case #%d: "%testcase+str(count))
    
