T = input()
output = []
for i in xrange(T):
    a = [ ['','','',''], ['','','',''], ['','','',''], ['','','',''] ]
    dot_count = 0
    for l in xrange(4):
        str = raw_input()
        for m in xrange(4):
            a[l][m] = str[m]
            if str[m] == '.':
                dot_count += 1
    raw_input() #Empty line
    for j in xrange(4):
        for k in xrange(4):
            if a[j][k] == 'T':
                Ti = j; Tj = k
                break;
    is_done = False
    # Check rows
    for j in xrange(4):
        if a[j][0] == '.' or a[j][1] == '.':
            continue;
        if a[j][0] != 'T':
            a[Ti][Tj] = a[j][0]
        else:
            a[Ti][Tj] = a[j][1]
        if a[j][0] == a[j][1] and a[j][1] == a[j][2] and a[j][2] == a[j][3]:
            output.append("%s won" % a[Ti][Tj])
            is_done = True
            break
        a[Ti][Tj] = 'T'
    if is_done:
        continue
    # Check columns
    for j in xrange(4):
        if a[0][j] == '.' or a[1][j] == '.':
            continue;
        if a[0][j] != 'T':
            a[Ti][Tj] = a[0][j]
        else:
            a[Ti][Tj] = a[1][j]
        if a[0][j] == a[1][j] and a[1][j] == a[2][j] and a[2][j] == a[3][j]:
            output.append("%s won" % a[Ti][Tj])
            is_done = True
            break
        a[Ti][Tj] = 'T'
    if is_done:
        continue
    # Check Diagonals
    if not (a[0][0] == '.' or a[1][1] == '.'):
        if a[0][0] != 'T':
            a[Ti][Tj] = a[0][0]
        else:
            a[Ti][Tj] = a[1][1]
        if a[0][0] == a[1][1] and a[1][1] == a[2][2] and a[2][2] == a[3][3]:
            output.append("%s won" % a[Ti][Tj])
            is_done = True
            continue
    if is_done:
        continue
    a[Ti][Tj] = 'T'
    if not (a[0][3] == '.' or a[1][2] == '.'):
        if a[0][3] != 'T':
            a[Ti][Tj] = a[0][3]
        else:
            a[Ti][Tj] = a[1][2]
        if a[0][3] == a[1][2] and a[1][2] == a[2][1] and a[2][1] == a[3][0]:
            output.append("%s won" % a[Ti][Tj])
            continue
    if dot_count:
        output.append("Game has not completed")
    else:
        output.append("Draw")
for i in xrange(len(output)):
    print "Case #%d: %s" %(i+1, output[i])

