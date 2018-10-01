f = open('A-large.in')
cases = int(f.readline())
a = []
for m in range(cases):
    stat=0
    for l in range(4):
        a.append([])
        temp = f.readline()
        for k in range(4):
            tempchar = temp[k:k+1]            
            a[l].append(tempchar)    
    f.readline()
    print "Case #{no}:".format(no=m+1),        
    chkcrossx=0
    chkcrossy=0
    chkcrossxx=0
    chkcrossyy=0
    allchar=0
    for pk in range(4):       
        chkx=0
        chky=0
        chkxx=0
        chkyy=0
        out = 0
        for lk in range(4):          
            if a[pk][lk] == 'X' or a[pk][lk] == 'T':
                chkx = chkx + 1
            if a[pk][lk] == 'O' or a[pk][lk] == 'T':
                chky = chky + 1
            if a[lk][pk] == 'X' or a[lk][pk] == 'T':
                chkxx = chkxx + 1
            if a[lk][pk] == 'O' or a[lk][pk] == 'T':
                chkyy = chkyy + 1
            if a[pk][lk] == 'O' or a[pk][lk] == 'T' or a[pk][lk] == 'X':
                allchar = allchar + 1;
    
            if chky == 4 or chkyy == 4: #or chkcrossy == 4:
                print "O won"
                out = 1;
                break
            if chkx == 4 or chkxx == 4: #or chkcrossx == 4:
                print "X won"
                out = 1
                break
        if out ==1 :
            break   
        if a[pk][pk] == 'X' or a[pk][pk] == 'T':
            chkcrossx = chkcrossx + 1
        if a[pk][pk] == 'O' or a[pk][pk] == 'T':
            chkcrossy = chkcrossy + 1
          
        if a[pk][3-pk] == 'X' or a[pk][3-pk] == 'T':
            chkcrossxx = chkcrossxx + 1
        if a[pk][3-pk] == 'O' or a[pk][3-pk] == 'T':
            chkcrossyy = chkcrossyy + 1        
    if chkcrossy == 4 or chkcrossyy == 4:
        print "O won"
    elif chkcrossx == 4 or chkcrossxx == 4:
        print "X won"
    elif allchar == 16 and out != 1:
        print "Draw"
    elif out != 1:
        print "Game has not completed"
    a=[]
f.close()
