
def solve(R, C, M):
    if len([m for m in M if '#' in m])==0:
        return '\n'.join([''.join(m) for m in M])
    for r in range(R):
        for c in range(C):
            if M[r][c]=='#':
                M1 = [m[:] for m in M]
                M1 = search(M1, R, C, r, c)
                if M1!=None:
                    return '\n'.join([''.join(m) for m in M1])
    return 'Impossible'

def search(M, R, C, r, c):
    if len([m for m in M if '#' in m])==0:
        return M
    if (r+1)<R and (c+1)<C and M[r+1][c]=='#' and M[r][c+1]=='#' and M[r+1][c+1]=='#':
        M1 = [m[:] for m in M]
        M1[r][c]='/'
        M1[r+1][c]='\\'
        M1[r][c+1]='\\'
        M1[r+1][c+1]='/'
        for rr in range(R):
            for cc in range(C):
                if M1[rr][cc]=='#':
                    M2 = search(M1, R, C, rr, cc)
                    if M2!= None:
                        return M2
                    else:
                        return None
        return M1
    else:          
        return None
        

input_file = 'A-large.in'
output_file = 'result.dat'
fin=open(input_file , 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    R,C = [int(x) for x in fin.readline().split()]
    M = [[c for c in fin.readline().strip()] for i in range(R)]
    ans = 'Case #%d:\n%s\n'%(t, solve(R,C,M))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()