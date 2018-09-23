import math

def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(int,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(out_list): return ' '.join(map(str,out_list))
imp="IMPOSSIBLE"

f_in=open('in.txt','r')
f_out=open('out.txt','w')
output=""
T=readint(f_in)

def add(c,i,j,table):
    table[i][j]=c
    return ' '.join([c,str(i+1),str(j+1)])+'\n'


for test in range (T):
    output+="Case #"+str(test+1)+": "
    row=readint_l(f_in)
    n=row[0]
    m=row[1]
    add_string=''
    adds=0
    table=[['.' for x in range(n)] for y in range(n)]
    for i in range (m):
        row=read_l(f_in)
        table[int(row[1])-1][int(row[2])-1]=row[0]
    #first row:
    if 'o' in table[0]:
        o_place=table[0].index('o')
    else:
        if('x' in table[0]):
            o_place = table[0].index('x')

            add_string+=add('o',0,o_place,table)
            adds+=1
        else:
            o_place = n-1

            add_string += add('o', 0, o_place,table)
            adds += 1
    for i in range(n):
        if (table[0][i]=='.'):

            add_string += add('+', 0, i,table)
            adds += 1
    #diagonal:
    for i in range(1,n,1):
        if (o_place-i>=0):
            add_string += add('x', i, o_place-i,table)
            adds += 1
        else:
            add_string += add('x', i, i,table)
            adds += 1
    #last row:
    for i in range(1, n-1, 1):
        add_string += add('+', n-1, i,table)
        adds += 1
    score=3*n-2
    if (n==1):
        score=2
    output+=list_to_str([score,adds])+'\n'+add_string

f_out.write(output)
f_out.close()
f_in.close()
