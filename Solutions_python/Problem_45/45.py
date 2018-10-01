import itertools

def count(cells,x):
    n=0
    j=x-1
    while j>=0 and cells[j]:       
        j-=1
        n+=1        
    j=x+1
    l=len(cells)
    while j<l and cells[j]:
        j+=1
        n+=1
    return n

def bribe(P,q):
    cells=[1]*P
    n=0    
    for i in q:         
        cells[i-1]=0
        n+=count(cells,i-1)
    return n
    
T=int(raw_input())
for case_no in range(1,T+1):
    P,Q=map(int, raw_input().split())
    q=map(int, raw_input().split())
    
    s=[]
    for x in itertools.permutations(q):
        n=bribe(P,x)
        s.append(n)
    
    print "Case #%d: %d" % (case_no, min(s))