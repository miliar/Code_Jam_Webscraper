NN=5
data = raw_input()
data2=data.split('\n')
Ncases=int(data2.pop(0))
data3=[[data2[i],data2[i+1],data2[i+2],data2[i+3]] for i in range(0,(Ncases)*NN,NN)]

def winset(case):
    size=len(case)
    if (size==2) and (('T' in case) and ('X' in case)):
        return [True,'X']
    elif (size==2) and (('T' in case) and ('O' in case)):
        return [True,'O']
    elif (size==1) and ('O' in case):

        return [True,'O']
    elif (size==1) and ('X' in case):
        return [True,'X']
    else:
        return [False]
    

def row(case,n):
    r=set(case[n])
    return winset(r)
    

def column(case,n):
    c=set([case[0][n],case[1][n],case[2][n],case[3][n]])
    return winset(c)

def diagonals(case):
    d1=set([case[0][0],case[1][1],case[2][2],case[3][3]])
    d2=set([case[0][3],case[1][2],case[2][1],case[3][0]])
    if winset(d1)[0]:
        return winset(d1)
    elif winset(d2)[0]:
        return winset(d2)
    else:
        return winset(d1)

def nowin(case):
    d=set("".join(case))
    if "." in d:
        return "Game has not completed"
    else:
        return "Draw"

def check(case):
    diag=diagonals(case)
    if diag[0]:
        return '{0} won'.format(diag[1])
    for i in range(0,4):
         if row(case,i)[0]:
             return '{0} won'.format(row(case,i)[1])
    for i in range(0,4):
        if column(case,i)[0]:
            return '{0} won'.format(column(case,i)[1])
    return nowin(case)


for i in range(0,Ncases):
    result=check(data3[i])
    print 'Case #{0}: {1}'.format(i+1,result) 
    
    
