'''
Created on May 20, 2011

@author: Phil
'''

import os
thisname = os.path.basename(__file__)
namefile = thisname.split('.')[0]

inpname = raw_input("File input: ")

fr = open(inpname, 'r')
fc = fr.read()
fr.close()

output = ""

lines = fc.split('\n')

numOfCases = int(lines[0])

lindex = 1
casenum = 0
while casenum<numOfCases:
    board = []
    for z in range(int(lines[lindex].split(' ')[0])):
        arr = []
        for c in lines[lindex+z+1]:
            arr.append(c)
        board.append(arr)
    tmpB = False
    i=0
    while i<len(board):
        j=0
        while j<len(board[i]):
            if board[i][j]=='#':
                if (len(board[i])-1)>j and (len(board)-1)>i:
                    if board[i][j+1]=='#' and board[i+1][j]=='#' and board[i+1][j+1]=='#':
                        board[i][j] = '/'
                        board[i][j+1] = '\\'
                        board[i+1][j] = '\\'
                        board[i+1][j+1] = '/'
                    else:
                        tmpB = True
                        break
                else:
                    tmpB = True
                    break
            j=j+1
        if tmpB:
            break
        i=i+1
    output = output + "Case #" + str(casenum+1)+":\n"
    if tmpB:
        output = output + "Impossible\n"
    else:
        for l in board:
            output = output + "".join(l)+"\n"

    lindex = lindex + int(lines[lindex].split(' ')[0])+1
    casenum = casenum+1


fw = open(inpname.split('.')[0] + '-out.txt', 'w')
fw.write(output)
fw.close()
