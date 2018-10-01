def flip(pan_str, side, num):

    pan = list(pan_str)
    # Left
    if(side == 0):
        for i in range(num):
            if(pan[i] == '+'):
                pan[i] = '-'
            else:
                pan[i] = '+'
    else:
        for i in range(num):
            if(pan[-1-i] == '+'):
                pan[-1-i] = '-'
            else:
                pan[-1-i] = '+'

    return ''.join(pan)


t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):

    inp = raw_input().split()
    # print inp
    pan = inp[0]
    flipper = int(inp[1])

    count = 0
    start = 0
    end = len(pan)-1
    over = False

    while('-' in pan[start:end+1]):

        if(end + 1 - start < flipper):
            try:
                pan = pan[:start] + flip(pan[start:end+1], 0, flipper) + pan[end+1:]
            except:
                pass

            if('-' in pan[start:end+1]):
                print "Case #{}: {}".format(i, 'IMPOSSIBLE')
                over = True
            break

        if(pan[start] == '-'):
            pan = pan[:start] + flip(pan[start:end+1], 0, flipper) + pan[end+1:]
            count += 1

        if(pan[end] == '-'):
            pan = pan[:start] + flip(pan[start:end+1], 1, flipper) + pan[end+1:]
            count += 1

        for ind in range(start, end+1):
            if(pan[ind] == '-'):
                start = ind
                break

        for ind in range(end, start-1, -1):
            if(pan[ind] == '-'):
                end = ind
                break

    if(over):
        continue

    print "Case #{}: {}".format(i, count)
