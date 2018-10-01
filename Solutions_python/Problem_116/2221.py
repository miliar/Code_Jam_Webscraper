##Tic-Tac-Tomek
##Michael Feliciano
#College of Charleston
# Small solution

files = ["test.in","A-small-attempt0.in","A-large.in"]
content = file(files[2])

cases = int(content.readline())

filename = "output.txt"
File = open(filename,'w')

for i in range(cases):
    if(i > 0):
        space = content.readline()
        
    mat = [[],[],[],[]]
    for e in range(4):
        mat[e]= content.readline().strip()
        
    ## Check for left diagonal victory
    ldVictory = False
    ld = []
    ld.append(mat[0][0])
    ld.append(mat[1][1])
    ld.append(mat[2][2])
    ld.append(mat[3][3])
    if('X' in ld and not 'O' in ld and not '.' in ld):
        File.write("Case #%d: %s" % (i+1,"X won" ) + "\n")
        ldVictory = True
        continue
    elif('O' in ld and not 'X' in ld and not '.' in ld):
        File.write("Case #%d: %s" % (i+1,"O won" ) + "\n")
        ldVictory = True
        continue

    ## Check for right diagonal victory
    rdVictory = False
    rd = []
    rd.append(mat[0][3])
    rd.append(mat[1][2])
    rd.append(mat[2][1])
    rd.append(mat[3][0])
    if('X' in rd and not 'O' in rd and not '.' in rd):
        File.write("Case #%d: %s" % (i+1,"X won" ) + "\n")
        rdVictory = True
        continue
    elif('O' in rd and not 'X' in rd and not '.' in rd):
        File.write("Case #%d: %s" % (i+1,"O won" ) + "\n")
        rdVictory = True
        continue

    ## Check for horizontal victory
    hVictory = False
    containsDot = False
    for h in mat:
        if("." in h):
            containsDot = True
        if('X' in h and not 'O' in h and not '.' in h):
            File.write("Case #%d: %s" % (i+1,"X won" ) + "\n")
            hVictory = True
            break
        elif('O' in h and not 'X' in h and not '.' in h):
            File.write("Case #%d: %s" % (i+1,"O won" ) + "\n")
            hVictory = True
            break
    
    if(hVictory == True):
        continue

    ## Check for vetical victory
    vVictory = False

    index = -1
    for m in range(4):
        index+=1
        attempt = []
        for f in range(4):
            attempt.append(mat[f][index])

        if('X' in attempt and not 'O' in attempt and not '.' in attempt):
            File.write("Case #%d: %s" % (i+1,"X won" ) + "\n")
            vVictory = True
            break
        elif('O' in attempt and not 'X' in attempt and not '.' in attempt):
            File.write("Case #%d: %s" % (i+1,"O won" ) + "\n")
            vVictory = True
            break
    if(vVictory == True):
        continue

##need to decide on draw vs game has no completed
    totalVictory = ldVictory or rdVictory or hVictory or vVictory
    if(containsDot == True and totalVictory == False):
        File.write("Case #%d: %s" % (i+1,"Game has not completed") + "\n")
    if(containsDot == False and totalVictory == False):
        File.write("Case #%d: %s" % (i+1,"Draw") + "\n")
        
File.close()
        
