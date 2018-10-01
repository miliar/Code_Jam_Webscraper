f = open('A-small-attempt0.in','r')
amount=int(f.readline())
writefile = open('result','w')
matrix=[]
case=1
while amount!=0:
    matrix[:]=[]
    result=''
    for i in range(4):
        matrix.append(f.readline())
    f.readline()
    for i in range(4):
        if '.' in matrix[i]:
            result='Game has not completed'
    if result=='':
        result='Draw'
    for i in range(4):
        if i==0:
            if matrix[i][i]!='.':
                curr=matrix[i][i]
            else:
                break
        elif matrix[i][i]!=curr and matrix[i][i]!='T':
            break
        elif i==3:
            result=curr+' won'
    for i in range(4):
        if i==0:
            if matrix[i][3-i]!='.':
                curr=matrix[i][3-i]
            else:
                break
        elif matrix[i][3-i]!=curr and matrix[i][3-i]!='T':
            break
        elif i==3:
            result=curr+' won'
    for i in range(4):
        for j in range(4):
            if j==0:
                if matrix[i][j]!='.':
                    curr=matrix[i][j]
                else:
                    break
            elif matrix[i][j]!=curr and matrix[i][j]!='T':
                break
            elif j==3:
                result=curr+' won'
    for i in range(4):
        for j in range(4):
            if j==0:
                if matrix[j][i]!='.':
                    curr=matrix[j][i]
                else:
                    break
            elif matrix[j][i]!=curr and matrix[j][i]!='T':
                break
            elif j==3:
                result=curr+' won'
    print('Case #'+str(case)+': '+result)
    writefile.write('Case #'+str(case)+': '+result+'\n')
    case+=1
    amount-=1
writefile.close()
