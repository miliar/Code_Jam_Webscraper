from math import *

def getcoor(n,A,B,C,D,x0,y0,M):
    X=x0
    Y=y0
    ll = []
    ll.append((X,Y))
    for i in range(1,n):
        X=(A*X+B) % M
        Y=(C*Y+D) % M
        ll.append((X,Y))
    return ll

def center(a,b,c):
    x = a[0]+b[0]+c[0]
    y = a[1]+b[1]+c[1]
    x *= 1.0
    y *= 1.0
    return (x/3.0,y/3.0)
    
def func(n,A,B,C,D,x0,y0,M):
    count = 0
    trees = getcoor(n,A,B,C,D,x0,y0,M)
    for i in range(0,len(trees)):
        for j in range(i,len(trees)):
            for k in range(j,len(trees)):
                if i == j or i == k or j == k:
                    continue
                c = center(trees[i],trees[j],trees[k])
                ix,iy = c
                ix = int(ix)
                iy = int(iy)
                if ix == c[0] and iy == c[1]:
                    count += 1
    return count







if __name__ == "__main__":
    T = int(raw_input())
    for i in range(T):
        line = raw_input()
        n,A,B,C,D,x0,y0,M = [int(ii) for ii in line.split(' ')]
        ans = func(n,A,B,C,D,x0,y0,M)
        print "Case #" + str(i+1) + ": " + str(ans)
