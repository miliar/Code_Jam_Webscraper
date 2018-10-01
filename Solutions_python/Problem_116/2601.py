def read_file(name="input.txt"):
    f = open(name)
    casecount = int(f.readline())

    cases = []

    for i in range(casecount):
        case = []
        while True:
            data = f.readline()
            if not data == '\n':
                case.append(list(data))
            else:
                break
        
        cases.append(case)

    return cases
def count(arr, char):
    count = 0
    for elem in arr:
        if elem == char:
            count = count + 1
    return count

def check_line(line):
    winrar = None
    c_x = count(line, 'X')
    c_o = count(line, 'O')
    c_t = count(line, 'T')
    c_e = count(line, '.')
    #print "derp:: %i x X, %i x O, %i x T, %i x ." % (c_x, c_o, c_t, c_e)
    if c_x == 4 or ( c_x == 3 and c_t == 1):
        winrar = 'X'
    if c_o == 4 or ( c_o == 3 and c_t == 1):
        winrar = 'O'
    return (winrar, c_e)

def determine_winrar(case):
    done = True

    # check horizontal
    for i in range(4):
        w, e = check_line(case[i])
        if not w == None:
            return (w, True)
        else:
            if e > 0:
                done = False
    # check vertical
    for i in range(4):
        arr = []
        for j in range(4):
            arr.append(case[j][i])
        w, e = check_line(arr)
        if not w == None:
            return (w, True)
        else:
            if e > 0:
                done = False
 
    # check diagonal
    arr = []
    for i in range(4):
        arr.append(case[i][i])
    
    w, e = check_line(arr)
    if not w == None:
        return (w, True)

    # check diagonal
    arr = []
    for i in range(4):
        arr.append(case[i][3-i])
    
    w, e = check_line(arr)
    if not w == None:
        return (w, True)

    return (None, done)

if __name__ == '__main__':
    cases = read_file("large.txt")
    i = 1
    for case in cases:
        w, d = determine_winrar(case)
        if not w == None:
            print "Case #%i: %s won" % (i,w)  
        else:
            if d:
                print "Case #%i: Draw" % i
            else:
                print "Case #%i: Game has not completed" % i
        i += 1
