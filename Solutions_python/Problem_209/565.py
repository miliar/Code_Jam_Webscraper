from math import pi

def syrup(L):

    m = 0
    # we try every potential first pancake
    for i in range(len(L)):

        tmp = list(L)
        surface = pi * tmp[i][0] * tmp[i][0] + 2 * pi * tmp[i][0] * tmp[i][1]

        tmp.pop(i)
        # we keep the best pancakes
        LS = list(reversed(sorted(tmp, key=lambda value: value[2])))
        PC = LS[:K-1]

        #and now sort them by radius
        PC = list(reversed(sorted(PC, key = lambda value: value[0])))

        while(len(PC)>0):
            # next pancakes only bring height
            surface += 2*pi*PC[0][0]*PC[0][1]
            PC.pop(0)

        if(surface > m):
            m = surface

    return m

t = int(input().strip())

for a in range(t):
    NK =input().strip()

    l = NK.split(' ')
    l = list(map(int, l))

    N = l[0]
    K = l[1]

    L = [(0,0,0)] * N

    for a0 in range(N):
        RH = input().strip()
        
        p = RH.split(' ')
        p = list(map(int, p))

        L[a0] = (p[0], p[1], p[0]*p[1])

    print("Case #",a+1, ": ", "{:.9f}".format(syrup(L)), sep='')
