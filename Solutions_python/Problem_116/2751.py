def checkHor(a):
    found = ''
    for i in range(4):
        prev = a[i][0][0]
        for ii in range(4):
            if ii > 0:
                if prev == 'T':
                    prev = a[i][0][ii]
                    continue
                if (a[i][0][ii] == prev or a[i][0][ii] == 'T') and ii == 3:
                    #print prev + str(' hor ')
                    return prev
                elif a[i][0][ii] == prev or a[i][0][ii]=='T':
                    continue
                else:
                    break
    return ''

def checkVert(a):
    prev = ''
    for i in range(4):
        for ii in range(4):
            if ii > 0:
                if prev == 'T':
                    prev = a[ii][0][i]
                    continue
                if ii == 3 and (a[ii][0][i] == prev or a[ii][0][i] == 'T'):
                    #print prev + str(' vert ')
                    return prev
                elif a[ii][0][i] == prev or a[ii][0][i]=='T':
                    continue
                else:
                    break
            else:
                prev = a[ii][0][i]
    return ''


def checkDiag(a):
    d1 = []
    d2 = []
    for i in range(3,-1,-1):
        d1.append(a[i][0][3-i])
    for i in range(4):
        d2.append(a[i][0][i])
    for i in range(len(d1)):
        if i > 0:
            if prev == 'T':
                prev = d1[i]
                continue
            if i==3 and (d1[i] == prev or d1[i] == 'T'):
                #print prev + str(' d1 ')
                return prev
            elif d1[i] == prev or d1[i] == 'T':
                continue
            else:
                break
        else:
            prev = d1[i]
    for i in range(len(d2)):
        if i > 0:
            if prev == 'T':
                prev = d2[i]
                continue
            if i==3 and (d2[i] == prev or d2[i] == 'T'):
                #print prev + str(' d2 ')
                return prev
            elif d2[i] == prev or d2[i] == 'T':
                continue
            else:
                break
        else:
            prev = d2[i]
    return ''
            
if __name__=='__main__':
    board = []
    case = 1
    cases = 0
    l = 0
    gameWon = inc = False
    infile = open('C:\\Users\\Intrex\\Downloads\\A-small-attempt2.in','r')
    outfile = open('C:\\Users\\Intrex\\Downloads\\probA_out.txt','w')
    f = infile.read().split('\n')
    for i in range(4):
        board.append([])
    for i in range(len(f)):
        if i==0:
            cases = int(f[i])
        if i > 0 and case <= cases:
            if f[i] != '':
                board[l].append(f[i])
                l+=1
                
            if f[i] == '':
                #print board
                outfile.write('{0}{1}: '.format('Case #',case))
                l=0
                h = checkHor(board[:])
                v = checkVert(board[:])
                d = checkDiag(board[:])
                if h != '' and h!='.':
                    outfile.write(h + ' won\n')
                    gameWon = True
                elif v != '' and v!='.':
                    outfile.write(v + ' won\n')
                    gameWon = True
                elif d != '' and d!='.':
                    outfile.write(d + ' won\n')
                    gameWon = True
                elif not gameWon:
                    for i in range(4):
                        if '.' in board[i][0]:
                            outfile.write('Game has not completed\n')
                            inc = True
                            break
                    if not inc:
                        outfile.write('Draw\n')
                board = []
                gameWon = False
                inc = False
                for i in range(4):
                    board.append([])
                case+=1
    infile.close()
    outfile.close()