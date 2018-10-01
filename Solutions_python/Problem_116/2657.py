import sys
from re import findall
caseNumber = int(input(""))
mapa = {}
for number in range(caseNumber):
    mapa[number] = []
data = sys.stdin.readlines()

j=0
for i in data:
    if i.strip():
        mapa[j].append(i.strip())
    else:
        j+=1

result = {}
for number in range(caseNumber):
    result[number+1] = [0, 0]

for index in mapa:
    winX = 0
    winO = 0
    if '.' in mapa[index][0]: result[index+1][1] += 1
    elif '.' in mapa[index][1]: result[index+1][1] += 1
    elif '.' in mapa[index][2]: result[index+1][1] += 1
    elif '.' in mapa[index][3]: result[index+1][1] += 1
    for rows in mapa[index]:
        if findall('[TX]{4}', rows):
            result[index+1][0] += 1
            winX=1
            break
        elif findall('[TO]{4}', rows):
            result[index+1][0] += 2
            winO=1
            break

    str1=""
    str2=""
    str3=""
    str4=""
    for rows in range(4):
        str1 += mapa[index][rows][0]
        str2 += mapa[index][rows][1]
        str3 += mapa[index][rows][2]
        str4 += mapa[index][rows][3]
        
    for cols in (str1, str2, str3, str4):
        if not winX and findall('[TX]{4}', cols):
            result[index+1][0] += 1
            break
        elif not winO and findall('[TO]{4}', cols):
            result[index+1][0] += 2
            break 
    if not winO and (mapa[index][0][0] == 'O' or mapa[index][0][0] == 'T') and (mapa[index][1][1] == 'O' or mapa[index][1][1] == 'T') and (mapa[index][2][2] == 'O' or mapa[index][2][2] == 'T') and (mapa[index][3][3] == 'O' or mapa[index][3][3] == 'T'):
        result[index+1][0] += 2
        winO=1
    elif not winX and (mapa[index][0][0] == 'X' or mapa[index][0][0] == 'T') and (mapa[index][1][1] == 'X' or mapa[index][1][1] == 'T') and (mapa[index][2][2] == 'X' or mapa[index][2][2] == 'T') and (mapa[index][3][3] == 'X' or mapa[index][3][3] == 'T'):
        result[index+1][0] += 1
        winX=1
    if not winO and (mapa[index][0][3] == 'O' or mapa[index][0][3] == 'T') and (mapa[index][1][2] == 'O' or mapa[index][1][2] == 'T') and (mapa[index][2][1] == 'O' or mapa[index][2][1] == 'T') and (mapa[index][3][0] == 'O' or mapa[index][3][0] == 'T'):
        result[index+1][0] += 2
        winO=1
    if not winX and (mapa[index][0][3] == 'X' or mapa[index][0][3] == 'T') and (mapa[index][1][2] == 'X' or mapa[index][1][2] == 'T') and (mapa[index][2][1] == 'X' or mapa[index][2][1] == 'T') and (mapa[index][3][0] == 'X' or mapa[index][3][0] == 'T'):
        result[index+1][0] += 1
        winX=1

for number in range(caseNumber):
    if result[number+1][0] == 1: print("Case #"+str(number+1)+": X won")
    elif result[number+1][0] == 2: print("Case #"+str(number+1)+": O won")
    else:
        if result[number+1][1] == 0: print("Case #"+str(number+1)+": Draw")
        else: print("Case #"+str(number+1)+": Game has not completed")
