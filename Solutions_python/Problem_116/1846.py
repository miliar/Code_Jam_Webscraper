def check(b,play,y,z):
    c = True
    for i in range(4):
        if (b[y][i] != play) and (b[y][i] != 'T'):
            c =False
    if c:
        return True
        
    c = True
   
    for i in range(4):
        if (b[i][z] != play) and (b[i][z] != 'T'):
            c=False
    if c:
        print(y,z)
        return True
    if (y == 0 and z ==0) or (y == 3 and z == 3):
        if (b[0][0] == play or b[0][0] == 'T') and (b[1][1] == play or b[1][1] == 'T') and (b[2][2] == play or b[2][2] == 'T') and (b[3][3] == play or b[3][3] == 'T'):
            return True
            
    if (y == 0 and z ==3) or (y == 3 and z == 0):
        if (b[0][3] == play or b[0][3] == 'T') and (b[1][2] == play or b[1][2] == 'T') and (b[2][1] == play or b[2][1] == 'T') and (b[3][0] == play or b[3][0] == 'T'):
            return True
            
    return False

        
                              
        
f = open("DATA1.txt")
g = open("OUT1.txt",'w')
n = f.readline().strip()
for x in range(int(n)):
    complete = True
    b = [[0]*4 for i in range(4)]
    for y in range(4):
        line = f.readline().strip()
        for z in range(4):
            b[y][z] = line[z]
            if b[y][z] == '.' :
                complete = False
    xwin = False
    ywin = False
    for y in range(4):
        for z in range(4):
            if b[y][z] == 'X' and xwin == False:
                xwin = check(b,'X',y,z)
            elif b[y][z] == 'O' and ywin == False:
                ywin = check(b,'O',y,z)
    print(complete)
    if xwin:
        g.write("Case #"+str(int(x+1))+": "+"X won"+"\n")
    elif ywin:
        g.write("Case #"+str(int(x+1))+": "+"O won"+"\n")
    elif complete:
        g.write("Case #"+str(int(x+1))+": "+"Draw"+"\n")
    else:
        g.write("Case #"+str(int(x+1))+": "+"Game has not completed"+"\n")
    f.readline()
        
                
    
g.close()
