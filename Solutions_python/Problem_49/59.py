def dist(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

def divide(seq):
    s = []
    for i in range(len(seq)**2):
        r,l = [],[]
        for j in range(len(seq)):
            bit=1<<j&i
            if bit==0:
                r.append(seq[j])
            else:
                l.append(seq[j])
        s.append((l,r))
    return s

def groupWidth(group):
    n = len(group)
    if n is 0:
        return 0
    if n is 1:
        return group[0][2]

    max_dist = -1
    for i in range(n-1):
        for j in range(i,n):
            d = dist(group[i], group[j]) + group[i][2] + group[j][2]
            if d > max_dist:
                max_dist = d
    return max_dist/2.0
                       
def solve(pts):
    gps = divide(pts)
    mw = 10000000000000000
    for gp in gps:
        lw, rw = groupWidth(gp[0]), groupWidth(gp[1])
        mw = min(mw, max(lw, rw))        
    return mw

fin=open('D-small-attempt1.in', 'r')
fout=open('out.txt', 'w')

N = int(fin.readline())
for i in range(1,N+1):
    L = int(fin.readline())
    pts = []
    for _ in range(L):
        pts.append([float(s) for s in fin.readline().split()])
    ans = 'Case #%d: %f'%(i, solve(pts))
    print(ans)
    fout.write(ans + '\n')
fin.close()
fout.close()
