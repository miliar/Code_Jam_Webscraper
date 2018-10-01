dct=[]

def checkRecl(x, y):
    for shift in range(1, len(str(y))):
        #print x, str(y)[shift:]+str(y)[:shift]
        if(str(x) == str(y)[shift:]+str(y)[:shift]):
            return True
    return False

def check2(x,y):
    if (x >= y):
        return False
    return True

def findRecl(i, A, B):
    array=[]
    if str(i)[0]=='0':
        return array
    
    for shift in range(1, len(str(i))):
        recl = str(i)[shift:]+str(i)[:shift]
        if(recl[0]=='0'):
            continue
        if(recl == str(i)):
            continue
        if(i < int(recl) <= B):
            dct.append([int(i), int(recl)])

def get(A, B):
    global dct
    dct=list()
    i = A
    while (i <= B):
        findRecl(i,A,B)
        i = i + 1

f = open('C-small-attempt0.in')
o = open('output.txt', 'w')

count = int(f.readline())
i = 1
while(i<=count):
    A, B = f.readline().strip().split()
    A = int(A)
    B = int(B)
    print A, B
    get(A,B)
    print len(dct)
    if (i==1):
        o.write('Case #{0}: {1}'.format(i, len(dct)))
    else:
        o.write('\nCase #{0}: {1}'.format(i, len(dct)))   
    i = i + 1
f.close()
o.close()
