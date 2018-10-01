f = open('Bsmall.in','r')
a = f.read()
b = a.split('\n')
del(b[-1])

f.close()


vector = [(0,1),  ## Up
          (1,0),  ## Right
          (-1,0), ## Left
          (0,-1)]  ## Down


## This is for small only.

def solve(l):
    a = list(map(int,l[0].split(' ')))
    N,M = a[0], a[1]
    output = []
    for i in xrange(1,len(l)):
        output += [l[i].split(' ')]

    visited = [[2 for i in xrange(N)] for j in xrange(M)]
    ##return visited,output



    # Check vertical lines.
    
    for i in xrange(M):
        l = []
        for j in xrange(N):
            l += output[j][i]

        for i in xrange(len(l)):
            if '1' in l:
                ## either all of the horizontal lines are '1's or
                ## all of the vertical lines are '1's.
                a = check_horizontal(l,M,N,output)
                if a == False:
                    if len(set(l)) == 2:
                        return 'NO'
    return 'YES'

def check_horizontal(l,M,N,output):
    x = []
    c = False
    for i in xrange(len(l)):
        if l[i] == '1':
            x += [i]

    #y = []

    for i in xrange(len(x)):
        y = []
        for j in xrange(M):
            y += output[x[i]][j]


        if len(set(y)) == 2:
            return False

    return True

g = open('BsmallOut','w')    

T = int(b[0])
i = 1
k = 1
while T > 0:
    N = list(map(int,b[i].split(' ')))[0]
    l = []
    for j in xrange(i, i + N + 1):
        l = l + [b[j]]
    s = solve(l)
    i += (N+1)
    T -= 1
    w = 'Case #%d: %s \n' % (k , s)
    g.write(w)
    k += 1
g.close()








    
