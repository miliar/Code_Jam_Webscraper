import re

#f = open('A-small-practice.in', 'r')
#f = open('A-small.in', 'r')
f = open('A-large.in', 'r')
fw = open('A.out', 'w')
lines = f.readlines()
T = int(lines.pop(0))


def Test1():
    # <->
    incomplete = False
    for line in Field:
        if re.search("[XT][XT][XT][XT]", line):
            return "X won"
        if re.search("[OT][OT][OT][OT]", line):
            return "O won"
        if re.search("\.", line):
            incomplete = True
    if incomplete:
        return "Game has not completed"
    else:
        return "Draw"

def Test2():
    #^
    for j in xrange(4):
        #print j, Field
        line = Field[0][j]+Field[1][j]+Field[2][j]+Field[3][j]
        if re.search("[XT][XT][XT][XT]", line):
            return "X won"
        if re.search("[OT][OT][OT][OT]", line):
            return "O won"
    return ""


def Test3():
    #/ \
    lines = []
    lines.append(Field[0][0]+Field[1][1]+Field[2][2]+Field[3][3])
    lines.append(Field[0][3]+Field[1][2]+Field[2][1]+Field[3][0])
    for line in lines:
        if re.search("[XT][XT][XT][XT]", line):
            return "X won"
        if re.search("[OT][OT][OT][OT]", line):
            return "O won"
    return ""        

def Output(CaseN, Status):
    outputLine = "Case #"+str(CaseN)+": "+Status
    fw.write(outputLine + "\n")


def ReadField():
    Field = []
    for i in xrange(4):
        Field.append(lines.pop(0))
    lines.pop(0)
    return Field

##################################

for i in xrange(T):
    Field = ReadField()
    t1 = Test1()
    if t1 == "X won" or t1 == "O won":
        Output(i+1, t1)
        continue

    t2 = Test2()
    if t2 == "X won" or t2 == "O won":
        Output(i+1, t2)
        continue

    t3 = Test3()
    if t3 == "X won" or t3 == "O won":
        Output(i+1, t3)
        continue

    Output(i+1, t1)
