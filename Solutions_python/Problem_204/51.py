from math import floor, ceil
from collections import deque

def solve(N, P, A, Q):
    #N - num ingredients
    #P - num packages
    #A - recipe of ratt.
    #Qij - quantity in jth package of ith ingredient

    Q2 = [] #Q2 ij  will be the range [a,b] of acc multipliers
    for a, q in zip(A, Q):
        buf = deque()
        for pkg in sorted(q):
            qq,rr = divmod(10 * pkg, 11 * a)
            lower = qq + (rr > 0)
            qq,rr = divmod(10 * pkg, 9 * a)
            upper = qq
            buf.append((lower, upper))
        Q2.append(buf)

    ans = 0
    #greedily choose
    while True:
        if not all(Q2): return ans
        lower = max(r[0][0] for r in Q2)
        upper = min(r[0][1] for r in Q2)
        if lower <= upper:
            for row in Q2:
                row.popleft()
            ans += 1
        else:
            row = min(Q2, key = lambda x: x[0][1])
            row.popleft()

###
def main():
    with open('in.txt','r') as fi, \
            open('out.txt', 'w') as fo:
        rr = lambda: fi.readline().strip()
        rrM = lambda: map(int,rr().split())
        for tc in xrange(1, 1 + int(rr())):
            N, P = rrM()
            A = rrM()
            Q = [rrM() for _ in xrange(N)]
            zeta = solve(N,P,A,Q)

            outstr = "Case #%i: " % tc + str(zeta)
            print outstr
            fo.write(outstr+'\n')
            
if __name__ == "__main__": main()
