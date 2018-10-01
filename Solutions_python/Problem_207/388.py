from math import *

def func(n,r,o,y,g,b,v):
    if b <= r+y and r <= b+y and y <= r+b:
        #print('here')
        l = []
        for i in range(r):
            l.append('R')
        ll = []
        for j in range(r):
            if b != 0:
                ll.append('B')
                b -= 1
            else:
                ll.append('Y')
                y -= 1
        if r == 0:
            ll.append('B')
            #print('here')
            b -= 1
        i = 0
        #print(l)
        #print(ll)
        #print('b ',b)
        #print('y ',y)
        while b != 0 or y != 0:
            #print('while')
            if i == len(ll):
                i = 0
            if ll[i][-1] == 'B' and y != 0:
                ll[i]+='Y'
                #print(ll)
                #print('b ',b)
                #print('y ',y)
                y -= 1
                continue
            elif ll[i][-1] == 'Y' and b!= 0:
                ll[i] += 'B'
                b -= 1
                continue
            elif ll[i][0] == 'B' and y != 0:
                ll[i] = 'Y' + ll[i]
                #print(ll)
                #print('b ',b)
               # print('y ',y)
                y -= 1
                continue
            elif ll[i][0] == 'Y' and b != 0:
                ll[i] = 'B' + ll[i]
                b -= 1
                continue
            i += 1
        lll = []

        for k in range(r):
            lll.append(l[k])
            lll.append(ll[k])
        ss = ''
        if r == 0:
            ss = ll[0]
        for k in range(len(lll)):
            ss += lll[k]
        return ss
    else:
        return "IMPOSSIBLE"

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n,r,o,y,g,b,v = [int(s) for s in input().split()]
    #print(n,r,o,y,g,b,v)
    print("Case #{}: {}".format(i, func(n,r,o,y,g,b,v)))
