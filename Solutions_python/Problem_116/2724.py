def checkox(lis,ch):
    i=0
    while i<4:
        j=0
        while j<4:
            if lis[i][j]== 'T':
                temp=list(lis[i])
                temp[j]=ch
                #print temp
                lis[i]="".join(temp)
            j+=1
        i+=1
    i=0
    #print lis
    if lis[0][0]==lis[1][1]==lis[2][2]==lis[3][3]==ch:
        return True
    if lis[0][3]==lis[1][2]==lis[2][1]==lis[3][0]==ch:
        return True
    while i<4:
        if lis[0][i]==lis[1][i]==lis[2][i]==lis[3][i]==ch:
            return True
        if lis[i][0]==lis[i][1]==lis[i][2]==lis[i][3]==ch:
            return True
        i+=1
    return False


def find_dot(lis):
    i=j=0
    while i<4:
        while j<4:
            if lis[i][j] is '.':
                return True
            j+=1
        i+=1
    return False

def checkgrid(lis):
    lis2=lis[:]
    lis3=lis[:]
    if checkox(lis2,'X'):
        return "X won"
    if checkox(lis3,'O'):
        return "O won"
    if find_dot(lis):
        return  "Game has not completed"
    return "Draw"

#l=['1','OOOX','O...','O...','T...']
file = open("A-small-attempt2.in")
l=[]
while 1:
	line=file.readline()
	if not line:
		break
	l.append(line)

num=int(l[0])
i=0
outs=[]
while i<num:
    grid=[]
    j=0
    while j<4:
       grid.append(l[5*i+1+j])
       j+=1
    res=checkgrid(grid)
    outs.append("Case #"+str(i+1)+": "+res)
    i+=1

for e in outs:
    print e
