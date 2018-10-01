

def b_move(seq, b ,b_curr, flag):
    if len(b) == 0:
        return seq, b ,b_curr, flag
    elif seq[0][0] == 'B' and b_curr == seq[0][1]:
        seq.pop(0)
        b.pop(0)
        flag = 1
        return seq, b ,b_curr, flag
    elif b_curr < b[0][1]:
        b_curr += 1
    elif b_curr > b[0][1]:
        b_curr -= 1
    elif b_curr == b[0][1]:
        return seq, b ,b_curr, flag
    return seq, b ,b_curr, flag

def o_move(seq, o ,o_curr, flag):
    if len(o) == 0:
        return seq, o ,o_curr
    elif seq[0][0] == 'O' and o_curr == seq[0][1] and flag == 0:
        seq.pop(0)
        o.pop(0)
        return seq, o ,o_curr
    elif o_curr < o[0][1]:
        o_curr += 1
    elif o_curr > o[0][1]:
        o_curr -= 1
    elif o_curr == o[0][1]:
        return seq, o ,o_curr
    return seq, o ,o_curr
                
input = open('A-large.in', 'r')
output = open('bot.out', 'w')

t = int(input.readline())
for case in range(1, t+1):
    line = input.readline().strip().split()
    n = int(line[0])
    
    b_curr = o_curr = 1
    b = []
    o = []
    seq = []

    for i in range(1, n*2, 2):
        seq.append([line[i], int(line[i+1])])
        if line[i] == 'B':
            b.append([line[i], int(line[i+1])])
        elif line[i] == 'O':
            o.append([line[i], int(line[i+1])])
        else:
            print "Error!"

    seconds = 0

    while seq:
        '''
        print seq
        print b, o
        print b_curr, o_curr
        print
        '''
        flag = 0
        seq, b ,b_curr, flag = b_move(seq, b ,b_curr, flag)
        seq, o ,o_curr = o_move(seq, o ,o_curr, flag)
        
        seconds += 1
    
    print 'Case #'+str(case)+':', seconds
    print
    output.write("Case #%s: %s\n" %(case, seconds))
