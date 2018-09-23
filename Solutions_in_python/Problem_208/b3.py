from heapq import *
fi=open("C:\\users\\Sergiy\\Downloads\\C-small-attempt4.in",'r')
#fi=open("C:\\users\\Sergiy\\Downloads\\C-large.in",'r')
fo=open("answer.txt",'w')

def calc(): 
    ans=[]    
    N,Q=map(int,fi.readline().split())
    ES=[tuple(map(int,fi.readline().split())) for _ in range(N)]
    D=[list(map(int,fi.readline().split())) for i in range(N)]
    E=[[] for i in range(N)] 
    
    for i in range(N):
        for j,x in enumerate(D[i]):
            if x>0:
                E[i].append((j,x))
    for _ in range(Q):
        U,V=map(int,fi.readline().split())
        U,V=U-1,V-1        
        ch=[(0,-ES[U][1],-ES[U][0],U)]
        T=[10**20]*N
        T[U]=0
        while len(ch):
            tim,spd,e,nom=heappop(ch)
            e,spd=-e,-spd
            if nom==V: ans.append('{:.9f}'.format(tim)); break
            for v,x in E[nom]:
                if e<x or tim+x/spd>=T[v]+100000: continue
                if tim+x/spd<T[v]: T[v]=tim+x/spd
                heappush(ch,(tim+x/spd,-spd,x-e,v))
                heappush(ch,(tim+x/spd,-ES[v][1],-ES[v][0],v))
                
    return ' '.join(ans)
        
for testNo in range(int(fi.readline())): 
    print("Case #{}: {}".format(testNo+1,calc()),file=fo)

fi.close()
fo.close()
print("Ok")