infile = open("DATA.txt")
infile = infile.readlines()
x = int(infile[0])
x*= 4
for iii in range(1, x + 4, 4):
    data = infile[iii:iii+4]
    for i, v in enumerate(data):
        data[i] = v.strip()
    xwin = False
    owin = False
    for i,v  in enumerate(data):
        for ii, vv in enumerate(v):
            if i == 0:
                if v[ii] == "X" and data[i+1][ii] == "X" and data[i+2][ii] == "X" and data[i+3][ii] == "X":
                    xwin = True
                    break
                elif v[ii] == "T" and data[i+1][ii] == "X" and data[i+2][ii] == "X" and data[i+3][ii] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i+1][ii] == "T" and data[i+2][ii] == "X" and data[i+3][ii] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i+1][ii] == "X" and data[i+2][ii] == "T" and data[i+3][ii] == "X":
                    xwin = True
                    break               
                elif v[ii] == "X" and data[i+1][ii] == "X" and data[i+2][ii] == "X" and data[i+3][ii] == "T":
                    xwin = True
                    break    
                elif v[ii] == "O" and data[i+1][ii] == "O" and data[i+2][ii] == "O" and data[i+3][ii] == "O":
                    owin = True
                    break
                elif v[ii] == "T" and data[i+1][ii] == "O" and data[i+2][ii] == "O" and data[i+3][ii] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i+1][ii] == "T" and data[i+2][ii] == "O" and data[i+3][ii] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i+1][ii] == "O" and data[i+2][ii] == "T" and data[i+3][ii] == "O":
                    owin = True
                    break               
                elif v[ii] == "O" and data[i+1][ii] == "O" and data[i+2][ii] == "O" and data[i+3][ii] == "T":
                    owin = True
                    break  
            if ii == 0:
                if v[ii] == "X" and data[i][ii+1] == "X" and data[i][ii+2] == "X" and data[i][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "T" and data[i][ii+1] == "X" and data[i][ii+2] == "X" and data[i][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i][ii+1] == "T" and data[i][ii+2] == "X" and data[i][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i][ii+1] == "X" and data[i][ii+2] == "T" and data[i][ii+3] == "X":
                    xwin = True
                    break               
                elif v[ii] == "X" and data[i][ii+1] == "X" and data[i][ii+2] == "X" and data[i][ii+3] == "T":
                    xwin = True
                    break    
                elif v[ii] == "O" and data[i][ii+1] == "O" and data[i][ii+2] == "O" and data[i][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "T" and data[i][ii+1] == "O" and data[i][ii+2] == "O" and data[i][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i][ii+1] == "T" and data[i][ii+2] == "O" and data[i][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i][ii+1] == "O" and data[i][ii+2] == "T" and data[i][ii+3] == "O":
                    owin = True
                    break               
                elif v[ii] == "O" and data[i][ii+1] == "O" and data[i][ii+2] == "O" and data[i][ii+3] == "T":
                    owin = True
                    break
            if i == 0 and ii == 0:
                if v[ii] == "X" and data[i+1][ii+1] == "X" and data[i+2][ii+2] == "X" and data[i+3][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "T" and data[i+1][ii+1] == "X" and data[i+2][ii+2] == "X" and data[i+3][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i+1][ii+1] == "T" and data[i+2][ii+2] == "X" and data[i+3][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i+1][ii+1] == "X" and data[i+2][ii+2] == "T" and data[i+3][ii+3] == "X":
                    xwin = True
                    break               
                elif v[ii] == "X" and data[i+1][ii+1] == "X" and data[i+2][ii+2] == "X" and data[i+3][ii+3] == "T":
                    xwin = True
                    break    
                elif v[ii] == "O" and data[i+1][ii+1] == "O" and data[i+2][ii+2] == "O" and data[i+3][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "T" and data[i+1][ii+1] == "O" and data[i+2][ii+2] == "O" and data[i+3][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i+1][ii+1] == "T" and data[i+2][ii+2] == "O" and data[i+3][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i+1][ii+1] == "O" and data[i+2][ii+2] == "T" and data[i+3][ii+3] == "O":
                    owin = True
                    break               
                elif v[ii] == "O" and data[i+1][ii+1] == "O" and data[i+2][ii+2] == "O" and data[i+3][ii+3] == "T":
                    owin = True
                    break  
            if i == 3 and ii == 0:
                if v[ii] == "X" and data[i-1][ii+1] == "X" and data[i-2][ii+2] == "X" and data[i-3][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "T" and data[i-1][ii+1] == "X" and data[i-2][ii+2] == "X" and data[i-3][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i-1][ii+1] == "T" and data[i-2][ii+2] == "X" and data[i-3][ii+3] == "X":
                    xwin = True
                    break
                elif v[ii] == "X" and data[i-1][ii+1] == "X" and data[i-2][ii+2] == "T" and data[i-3][ii+3] == "X":
                    xwin = True
                    break               
                elif v[ii] == "X" and data[i-1][ii+1] == "X" and data[i-2][ii+2] == "X" and data[i-3][ii+3] == "T":
                    xwin = True
                    break    
                elif v[ii] == "O" and data[i-1][ii+1] == "O" and data[i-2][ii+2] == "O" and data[i-3][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "T" and data[i-1][ii+1] == "O" and data[i-2][ii+2] == "O" and data[i-3][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i-1][ii+1] == "T" and data[i-2][ii+2] == "O" and data[i-3][ii+3] == "O":
                    owin = True
                    break
                elif v[ii] == "O" and data[i-1][ii+1] == "O" and data[i-2][ii+2] == "T" and data[i-3][ii+3] == "O":
                    owin = True
                    break               
                elif v[ii] == "O" and data[i-1][ii+1] == "O" and data[i-2][ii+2] == "O" and data[i-3][ii+3] == "T":
                    owin = True
                    break                
    if owin:
        print "Case #%i: O won"%(iii/4+1)
    elif xwin:
        print "Case #%i: X won"%(iii/4+1)
    else:
        temp = 0
        for i in data:
            if i.count(".") == 0:
                temp += 1
        if temp == 4:
            print "Case #%i: Draw"%(iii/4+1)
        else:
            print "Case #%i: Game has not completed"%(iii/4+1)
                