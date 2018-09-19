def vypis():
    s = input('')
    z = s.split()
    R = int(z[0])
    C = int(z[1])
    z = []
    for j in range(R):
        s = input('')
        z2 = []
        for k in range(C):
            z2.append(s[k])
        z.append(z2)
    for j in range(R):
        for k in range(C):
            if (z[j][k] == '#'):
                z[j][k] = '/'
                if ((R-1 == j) or (C-1 == k)):
                    return False
                if (z[j][k+1] == '#'): 
                    z[j][k+1] = '\\'
                else:
                    return False
                if (z[j+1][k] == '#'): 
                    z[j+1][k] = '\\'
                else:
                    return False
                if (z[j+1][k+1] == '#'): 
                    z[j+1][k+1] = '/'
                else:
                    return False
    for j in range(R):
        for k in range(C):
            print(z[j][k],end='')
        print()    
 
T = int(input(''))
for i in range(T):
    print('Case #'+str(i+1)+': ')
    if (vypis() == False):
        print('Impossible')