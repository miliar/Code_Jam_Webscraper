# your code goes here
from sys import stdin

def tidy(k):
    l = k%10
    k=int(k/10)
    while k>0:
        c = k%10
        if l<c: return False
        k=int(k/10)
        l=c
    return True

t = int(stdin.readline().strip())
for iii in range(t):
        k = int(stdin.readline().strip())
        while not tidy(k):
            k-=1
        print('Case #{0}: {1}'.format(iii+1,k))
        
