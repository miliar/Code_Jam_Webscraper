f = open('B large input.in','r')
a = f.read()
f.close()
b = a.split('\n')
del(b[-1])

def decompose(n):
    #n is an int
    if n == 0:
        return [[0,0,0]]
    elif n == 1:
        return [[0,0,1]]
    elif n == 2:
        return [[0,1,1],[0,0,2]]
    
    elif n%3 == 0:
        m = int(n/3)
        if m <= 9:
            return [[m,m,m],[m-1,m,m+1]]
        return [[m,m,m]]
    elif n%3 == 1:
        m = int((n-1)/3)
        return [[m,m,m+1],[m-1,m+1,m+1]]
        
    elif n%3 == 2:
        m = int((n-2)/3)
        if m <= 8:
            return [[m,m+1,m+1],[m,m,m+2]]
        return [[m,m+1,m+1]]

def surprising(l):
    a,b = l[0],l[2]
    if a + 2 == b:
        return True
    else:
        return False


def solve(s):
    l = list(map(int,s.split(' ')))
    N,S,p = l[0],l[1],l[2]
    y = []
    for i in range(3,3+N):
        y = y + [decompose(l[i])]
    max2 = 0
    max1 = 0
    for i in range(len(y)):
        if len(y[i]) == 1:
            if y[i][0][2] >= p:
                max2 = max2 + 1
                
        else:
            if y[i][0][2] >= p:
                max2 = max2 + 1
            elif y[i][0][2] < p and y[i][1][2] >= p:
                max1 = max1 + 1
    x = (N-max2) - max1
    if S < max1 + x:
        if S < max1:
            return S + max2
        else:
            return max1 + max2
    elif S == max1 + x:
        return max1 + max2
    else:
        return max1 + max2

g = open('B large Output.txt','w')
N = int(b[0])
for i in range(1,N+1):
    x = solve(b[i])
    s = "Case #"+str(i) + ': '+ str(x) + '\n'
    g.write(s)
    #print(s)

g.close()
