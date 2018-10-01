def caseSolved(caseNum, res, is_Empty):
    answer_x = "X won"
    answer_o = "O won"
    answer_none = "Draw"
    answer_progress = "Game has not completed"
    if res=='X':
        return 'Case #{}: {}'.format(caseNum, answer_x)
    elif res=='O':
        return 'Case #{}: {}'.format(caseNum, answer_o)
    elif is_Empty:
        return 'Case #{}: {}'.format(caseNum, answer_progress)
    else:
        return 'Case #{}: {}'.format(caseNum, answer_none)

def checkLine(lineToCheck):
    X_win = True;
    O_win = True;
    is_empty = False;
    for sm in lineToCheck:
        if sm=='.':
            X_win = False
            O_win = False
            is_empty = True
        elif sm=='O':
            X_win = False
        elif sm=='X':
            O_win = False

    if(is_empty): return "E"
    elif(X_win): return "X"
    elif(O_win): return "O"
    else: return "-"


f = open("input.txt")
content = f.readlines()
nl = int(content[0])*5
cur = 1
caseNum = 1;
output = ""
while cur<nl:
    is_empty = False
    stringsToCheck = [content[cur][0]+content[cur+1][1]+content[cur+2][2]+content[cur+3][3],
                      content[cur][3]+content[cur+1][2]+content[cur+2][1]+content[cur+3][0],
                      content[cur], content[cur+1], content[cur+2], content[cur+3],
                      content[cur][0]+content[cur+1][0]+content[cur+2][0]+content[cur+3][0],
                      content[cur][1]+content[cur+1][1]+content[cur+2][1]+content[cur+3][1],
                      content[cur][2]+content[cur+1][2]+content[cur+2][2]+content[cur+3][2],
                      content[cur][3]+content[cur+1][3]+content[cur+2][3]+content[cur+3][3],
                    ]
    cnt = 0
    res = '-'
    while res=='-' and cnt<len(stringsToCheck):
        res = checkLine(stringsToCheck[cnt])
        if(res=='E'):
            is_empty = True
            res = '-'
        cnt = cnt + 1


    output = output + caseSolved(caseNum, res, is_empty) + '\n'
    caseNum = caseNum + 1

    cur = cur + 5


f = open('output.txt','w')
f.write(output)