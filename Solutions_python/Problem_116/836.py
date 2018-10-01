#!/user/bin/python

def check_unique(temp):
    unique = list(set(temp))
    if len(unique) == 1 :
        if unique[0] != '.':
            return unique[0]
    elif len(unique) == 2:
        if 'T' in unique:
            if 'X' in unique:
                return 'X'
            if 'O' in unique:
                return 'O'

def check_one_test(fo) :
    data = []
    diag_1 = []
    diag_2 = []
    flag = 0
    for i in range(0,4):
        data.append(list(fo.readline().strip()))
    fo.readline()
    for i in range(0,4):
        col = []
        ret = check_unique(data[i])
        if ret:
            return ret
        for j in range(0,4):
            col.append(data[j][i])
        ret = check_unique(col)
        if ret:
            return ret
        diag_1.append(data[i][i])
        diag_2.append(data[i][3-i]) 
        if '.' in data[i]: 
            flag = 1
    ret = check_unique(diag_1)
    if ret:
        return ret
    ret = check_unique(diag_2)
    if ret:
        return ret
    if flag == 0:
        return 'D'
    else:
        return '.'


fo = open("input", "r")
fw = open("output", "w")
no_of_cases = int(fo.readline().strip())
#print no_of_cases
count = 1
while no_of_cases:
    winner = ''
    string = ''
    winner = check_one_test(fo)
    if winner == '.':
        string = "Game has not completed"
    elif winner == 'D':
        string = "Draw"
    else:
        string = winner + " won"
    fw.write("Case #" + str(count) + ": " + string + "\n")
    print winner
    no_of_cases =  no_of_cases - 1
    count = count + 1

fo.close
fw.close