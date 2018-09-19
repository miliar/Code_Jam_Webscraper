import os, sys

ruler = [10,100,1000,10000,100000,1000000,10000000]
def numlen(num):
    last = 0
    for r in ruler:
        if num < r:
            return last
        last = r
    
def shift(a):
    if a%10:
        return (a/10) + numlen(a)*(a%10)
    else:
        return -1

def make_pairs(A,B):
    all = set()
    for i in range(A,B+1):
        t = i
        while True:
            t = shift(t)
            if i == t or t==-1:
                break
            else:
                if i>=A and i<= B and t >= A and t <= B:
                    all.add((min(i,t),max(i,t)))
                
    return len(all)

def main():
    ""
    
    
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(1,n+1):
        r = sys.stdin.readline().split(' ')
        A = int(r[0])
        B = int(r[1])
        print "Case #%d: %d" % (i, make_pairs(A,B))
