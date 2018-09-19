import string
def test():
    i=1
    f=open('A-large.in','r')
    T=int(f.readline())
    while i<T+1:
        temp=[]
        for a in f:
            if a!='\n':
                a=string.replace(a,'\n','')
                temp.append(a)
            else:
                break
        print "Case #"+str(i)+": " +game(temp)
        i+=1

def win(a):
    for i in a:
        if i=='XXXX' or i=='XXXT' or i=='XXTX' or i=='XTXX' or i=='TXXX':
            return 'X'
        elif i=='OOOO' or i=='OOOT' or i=='OOTO' or i=='OTOO' or i=='TOOO':
            return 'O'
        else:
            continue
        return False

def column_check(a):
    a_col=[]
    for k in range(4):
        i=''
        for j in range(4):
            i=i+a[j][k]
            j+=1
        a_col.append(i)
        k+=1
    return win(a_col)

def diagonal_check1(a):
    i=''
    a_dia=[]
    for j in range(4):
        i=i+a[j][j]
        j+=1
    a_dia.append(i)
    return win(a_dia)

def diagonal_check2(a):
    i=''
    a_dia=[]
    j=3
    k=0
    while j>=0:
        while k<4:
            i=i+a[k][j]
            j-=1
            k+=1
    a_dia.append(i)
    return win(a_dia)
        
def incomplete(a):
    i=''
    for j in range(4):
        for k in range(4):
            i=i+a[j][k]
            k+=1
        j+=1
    for b in i:
        if b=='.':
            return True
            break
        else:
            continue

def row_check(a):
    return win(a)

def game(a):
    m=row_check(a)
    if m!=False:
        if m=='X':
            return 'X won'
        elif m=='O':
            return 'O won'
    n=column_check(a)
    if n!=False:
        if n=='X':
            return 'X won'
        elif n=='O':
            return 'O won'
    o=diagonal_check1(a)
    if o!=False:
        if o=='X':
            return 'X won'
        elif o=='O':
            return 'O won'
    p=diagonal_check2(a)
    if p!=False:
        if p=='X':
            return 'X won'
        elif p=='O':
            return 'O won'
    y=incomplete(a)
    if y==True:
        return 'Game has not completed'
    else:
        return 'Draw'
    
            
        
    

        
