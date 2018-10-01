'''
Created on 2013-4-14

@author: Martin
'''

def decide(field):
    # 3: X 2: O 1: Draw 0: unfinished
    # row
    for i in range(4):
        sum = 0
        mul = 1
        for j in range(4):
            sum = sum + field[i][j]
            mul = mul * field[i][j]
        # end for
        if (sum == 3 and mul == 0) or (sum == 4):
            return 3
        elif (sum == -3 and mul == 0) or (sum == -4):
            return 2
    # col
    for j in range(4):
        sum = 0
        mul = 1
        for i in range(4):
            sum = sum + field[i][j]
            mul = mul * field[i][j]
        if (sum == 3 and mul == 0) or (sum == 4):
            return 3
        elif (sum == -3 and mul == 0) or (sum == -4):
            return 2
    # X
    sum = field[0][0]+field[1][1]+field[2][2]+field[3][3]
    if sum == 3 or sum == 4:
        return 3
    elif sum==-3 or sum==-4:
        return 2
    sum = field[0][3]+field[1][2]+field[2][1]+field[3][0]
    if sum == 3 or sum == 4:
        return 3
    elif sum==-3 or sum==-4:
        return 2
    sum = 0
    for i in range(4):
        for j in range(4):
            sum = sum + field[i][j]
    if sum<=20:
        return 1
    else:
        return 0

def solution(numOfCase, c):
    resDic = {}
    curRow = 1
    for countNum in range(numOfCase):
#        print countNum
        curField = [[0 for col in range(4)] for row in range(4)]
        tRow = curRow
        for ti in range(4):
            for tj in range(4):
                tempCh = c[tRow][tj]
                if tempCh == "X":
                    curField[ti][tj] = 1
                elif tempCh == "O":
                    curField[ti][tj] = -1
                elif tempCh == "T":
                    curField[ti][tj] = 0
                else:
                    curField[ti][tj] = 555
            tRow = tRow + 1
        # end for
#        print curField
        res = decide(curField)
        if res == 3:
            resDic[countNum] = "X won"
        elif res == 2:
            resDic[countNum] = "O won"
        elif res == 1:
            resDic[countNum] = "Draw"
        elif res == 0:
            resDic[countNum] = "Game has not completed"
        curRow = curRow + 5
    # end for
    return resDic
        


if __name__ == "__main__":
    f = open("A-large.in")
    c = f.read()
    c = c.split("\n");
    numOfCase = int(c[0])
#    print numOfCase
    resDic = solution(numOfCase, c)
    for i in resDic:
        resDic[i] = "Case #" + str(i+1) + ": " + resDic[i]
    # print resDic
    f.close()
    g = open("out.out","w")
    for i in resDic:
        if (i == numOfCase-1):
            g.write(resDic[i])
        else:
            g.write(resDic[i] + "\n")
    g.close