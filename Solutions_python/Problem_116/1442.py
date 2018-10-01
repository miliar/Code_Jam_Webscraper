import sys
import re

xwinpat = re.compile('[XT][XT][XT][XT]')
owinpat = re.compile('[OT][OT][OT][OT]')
dotpat = re.compile('.*\..*')


inputf = open('in.txt', 'r')
outf = open('out.txt', 'w')

case = int(inputf.readline())

for case in range(1, case+1):
    mapstr = ["","","",""]
    rowstr = ["","","",""]
    
    mapstr[0] = inputf.readline().replace('\n','')
    mapstr[1] = inputf.readline().replace('\n','')
    mapstr[2] = inputf.readline().replace('\n','')
    mapstr[3] = inputf.readline().replace('\n','')

    print mapstr

    for i in range(4):
        rowstr[i] = mapstr[0][i]+mapstr[1][i]+mapstr[2][i]+mapstr[3][i]    

    dgs = mapstr[0][0]+mapstr[1][1]+mapstr[2][2]+mapstr[3][3]
    rdgs = mapstr[3][0]+mapstr[2][1]+mapstr[1][2]+mapstr[0][3]
    
    fullstring = mapstr[0]+mapstr[1]+mapstr[2]+mapstr[3]

    won = False

    outf.write("Case #%d: " % case)

    for i in range(4):
        if won:
            break
        if xwinpat.match(mapstr[i]):
            outf.write('X won\n')
            won = True
        if owinpat.match(mapstr[i]):
            outf.write('O won\n')
            won = True
        if not won:
            if xwinpat.match(rowstr[i]):
                outf.write('X won\n')
                won = True
            if owinpat.match(rowstr[i]):
                outf.write('O won\n')
                won = True

    if not won:
        if xwinpat.match(dgs) or xwinpat.match(rdgs):
            outf.write('X won\n')
            won = True

        if owinpat.match(dgs) or owinpat.match(rdgs):
            outf.write('O won\n')
            won = True

    if not won:
        if dotpat.match(fullstring):
            outf.write('Game has not completed\n')
        else:
            outf.write('Draw\n')
            
    inputf.readline();

outf.close()
