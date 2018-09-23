def parse(a):
    down=0
    up=0
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            up=i
        if a[i]<a[i-1]:
            down=i
            break
    if down ==0:
        return a
    elif up==0 and a[0]=='1':
        return '9'*(len(a)-1)
    else:
        return a[:up]+str(int(a[up])-1)+'9'*(len(a)-1-up)


def small_fill(matrix, R, C):
    for i in range(R):
        for x in matrix[i]:
            if x != '?':
                H=x
            for j in range(matrix[i].find(H)):
                matrix[i][j] = H
            break
        for j in range(C):
            if matrix[i][j] == '?':
                matrix[i][j] = H
            else:
                H=matrix[i][j]
    return matrix
                    
def big_fill(matrix, R):
    index = 0
    for i in range(R):
        if matrix[i][0] == '?':
            index =i
            break
    for j in range(index):
        matrix[j]=matrix[index]
    H=matrix[index]
    for j in range(index+1,R):
        if matrix[j][0] == '?':
            matrix[j]=H
        else:
            H=matrix[j]
    return matrix
        
    


f=open("C:\Users\ronnie.frydberg\Desktop\codejam\test.in",'r')
g=open('test.out','w')
N=int(f.readline())
for c in range(1,N+1):
    R,C=[int(s) for s in f.readline().split(" ")]
    f.write("Case #{}:\n".format(c))
    matrix = [[x for x in f.readline()] for y in range(R)]
    matrix = small_fill(matrix,R,C)
    matrix = big_fill(matrix,R)    
    for i in range(R):
        f.write("".join(matrix[i]))
        if i<R-1:
            f.write('\n')




    
