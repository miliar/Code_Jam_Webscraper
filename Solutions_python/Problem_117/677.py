def ary():
    return [int(e) for e in raw_input().split()]

def solve(t, N, M, dat):
    rc = True
    R = []
    for i in range(N):
        R.append(max(dat[i]))
    
    C = [0]*M
    for i in range(M):
        m = 0
        for j in range(N):
            if dat[j][i] > m:
                m = dat[j][i]
        C[i] = m

    for i in range(N):
        for j in range(M):
            if R[i] > dat[i][j] and C[j] > dat[i][j]:
                rc = False
                break
        if not rc:
            break
            
    if rc:
        print 'Case #%d: %s'%(t, 'YES')
    else:
        print 'Case #%d: %s'%(t, 'NO')
    
def main():
    T = int(raw_input())
    for t in range(1, T+1):
        N, M = ary()
        dat = []
        for i in range(N):
            dat.append(ary())
        solve(t, N, M, dat)
        
main()