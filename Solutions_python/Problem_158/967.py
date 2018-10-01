#!/usr/bin/python
def solve():
    T = int(raw_input())
    for t in xrange(0,T):
        mn = (0,1,1,2,3)
        x,r,c = [int(k) for k in raw_input().split()]
        if r>0 and c>0 and (r*c)%x==0 and (r>=x or c>=x) and x<7 :
            if x<3 or (r>=mn[x] and c>=mn[x]) : w='GABRIEL'
            else : w='RICHARD'
        else : w='RICHARD'
        print 'Case #{}: {}'.format(t+1,w)

if __name__ == "__main__":
    solve()

