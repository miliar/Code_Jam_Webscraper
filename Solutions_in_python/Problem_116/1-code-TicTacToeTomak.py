type = 'large'
fi = open('1-input-%s.in' % type, 'r')
fo = open('1-outut-%s' % type, 'wb')
num_games = int(fi.readline())

print num_games
for T in xrange(1, num_games + 1):
    # Read board
    B = []
    for i in xrange(4):
        B.append(list(fi.readline().rstrip('\r\n')))
    fi.readline()

    # Add rotated board & diagonals
    B += zip(*B[::-1])
    B.append([B[0][0], B[1][1], B[2][2], B[3][3]])
    B.append([B[0][3], B[1][2], B[2][1], B[3][0]])

    # Look for winner
    winner = None
    incomplete = False
    for i in xrange(10):
        line = ''.join(B[i])
        if ((line == 'XXXX') or ((line.count('X') == 3) and (line.find('T') > -1))):
            winner = 'X'
            break
        elif ((line == 'OOOO') or ((line.count('O') == 3) and (line.find('T') > -1))):
            winner = 'O'
            break
        elif ((not incomplete) and (line.find('.') > -1)):
            incomplete = True

    # Output message
    if (not winner == None):
        msg = '%s won' % winner
    elif (incomplete):
        msg = 'Game has not completed'
    else:
        msg = 'Draw'
    output = 'Case #%d: %s' % (T, msg)
    print output
    fo.write('%s\n' % output)


fi.close()
fo.close()