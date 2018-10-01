(input,out)=(open("in","r"),open("out","w"))
cases=int(input.readline())
def get_c(x):
    if x==4:
        return '/'
    if x==5:
        return '\\'
    if x==6:
        return '\\'
    if x==7:
        return '/'
    else: return '.'
for s in xrange(cases):
    out.write('Case #%s:\n'% (s+1).__str__())
    matrix=[]
    (n,m)=[int(x) for x in list(input.readline().strip().split(' '))]
    for i in range(n):
        line=[0 if x=='.' else 1 for x in list(input.readline().strip())]
        matrix.append(line)
    for i in range(n-1):
        for j in range(m-1):
            if i>=n or j>=m: continue
            if matrix[i][j]==1 and matrix[i+1][j]==1 and matrix[i+1][j+1]==1 and matrix[i][j+1]==1:
                matrix[i][j]=4
                matrix[i+1][j]=6
                matrix[i+1][j+1]=7
                matrix[i][j+1]=5
                j+=1
    flag= False
    for i in range(n):
        if flag : break
        if 1 in matrix[i]:
            out.write('Impossible\n')
            flag=True
            break
    if flag: continue
    for i in range(n):
        line=''.join([get_c(x) for x in matrix[i]])
        out.write('%s\n'% line)





