def xwon(i):
    return "Case #"+str(i)+": X won\n"
def owon(i):
    return "Case #"+str(i)+": O won\n"

output = ""
#x = input()
f = open('test', 'r')
x = int(f.readline())
for i in range(0,x):
    dots = 0
    found = False
    lines = list()
    lines.append(f.readline())
    lines.append(f.readline())
    lines.append(f.readline())
    lines.append(f.readline())
    
    # check horizontal
    for line in lines:
        numberX = 0
        numberO = 0
        for x in line:
            if x == "X":
                numberX += 1
            elif x == "O":
                numberO += 1
            elif x == "T":
                numberX += 1
                numberO += 1
            elif x == ".":
                dots += 1
        if numberX == 4:
            output += xwon(i+1)
            found = True
        elif numberO == 4:
            output += owon(i+1)
            found = True
    # check vertical
    if not found:
        for i2 in range(0,4):
            numberX = 0
            numberO = 0
            for j in range(0,4):   
                if lines[j][i2] == "X":
                    numberX += 1
                elif lines[j][i2] == "O":
                    numberO += 1
                elif lines[j][i2] == "T":
                    numberX += 1
                    numberO += 1
            if numberX == 4:
                output += xwon(i+1)
                found = True
            elif numberO == 4:
                output += owon(i+1)
                found = True
    if not found:
        numberX = 0
        numberO = 0
        for k in range(0,4): 
            #print lines[k][k]
            if lines[k][k] == "X":
                numberX += 1
            elif lines[k][k] == "O":
                numberO += 1
            elif lines[k][k] == "T":
                numberX += 1
                numberO += 1
            #print "Case#"+str(i)+"numberX"+str(numberX)+"numberO"+str(numberO)
            if numberX == 4:
                output += xwon(i+1)
                found = True
            elif numberO == 4:
                output += owon(i+1)
                found = True
    if not found:
        numberX = 0
        numberO = 0
        for h in range(0,4):
            if lines[h][3-h] == "X":
                numberX += 1
            elif lines[h][3-h] == "O":
                numberO += 1
            elif lines[h][3-h] == "T":
                numberX += 1
                numberO += 1
            if numberX == 4:
                output += xwon(i+1)
                found = True
            elif numberO == 4:
                output += owon(i+1)
                found = True
    if not found and dots == 0:
        output += "Case #"+str(i+1)+": Draw\n"
    if not found and dots > 0:
        output += "Case #"+str(i+1)+": Game has not completed\n"
    x = f.readline()
text_file = open("out.txt", "w")
text_file.write(output)
text_file.close()
        
    
    