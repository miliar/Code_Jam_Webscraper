import sys
In = open('D:\\Workspace\\Google Code Jam\\D-small-attempt3.in', 'r')
Out = open('D:\Workspace\Google Code Jam\Out.py', 'w')
T = int(In.readline())
for ttt in range(T):
    x, r, c = In.readline().split()
    x = int(x)
    r = int(r)
    c = int(c)
    x_min = x - x/2
    winner = 'RICHARD'
    if r * c % x != 0:
        winner = 'RICHARD'
    elif x == 3 and r*c == 3 or x == 4 and r*c <= 8:
        winner = 'RICHARD'
    else:
        winner = 'GABRIEL'
        
    Out.write('Case #{}: {}\n'.format(ttt+1, winner))
    
In.close()
Out.close()