
def game_state(SC):
    if ((SC['X'] == 4)|((SC['X'] == 3)&(SC['T'] == 1))):
        return 0
    elif ((SC['O'] == 4)|((SC['O'] == 3)&(SC['T'] == 1))):
        return 1
    elif (SC['.'] == 0):
        return 2
    else:
        return 3
          

def check_row(data):
    rdata = []
    for c in range(len(data)):
        SC = {'X' : 0, 'O' : 0, 'T' : 0, '.' : 0}
        for t in data[c]:
            SC[t] = SC[t] + 1
        state = game_state(SC)
        if ((state == 0)|(state == 1)):
            return state
        rdata.append(state)
    if (rdata == [2]*len(data)):
        return 2
    return 3


def check_col(data):
    cdata = []
    for c in range(4):
        SC = {'X' : 0, 'O' : 0, 'T' : 0, '.' : 0}
        for t in data:
            SC[t[c]] = SC[t[c]] + 1
        state = game_state(SC)
        if ((state == 0)|(state == 1)):
            return state
        cdata.append(state)
    if (cdata == [2, 2, 2, 2]):
        return 2
    return 3


def checker(data):
    cum_states = []
    state = check_row(data)
    if ((state == 0)|(state == 1)):
        return "X won" if state == 0 else "O won"
    else:
        cum_states.append(state)
        state = check_col(data)
        if ((state == 0)|(state == 1)):
            return "X won" if state == 0 else "O won"
        else:
            cum_states.append(state)
            t1 = [data[0][0], data[1][1], data[2][2], data[3][3]]
            t2 = [data[0][3], data[1][2], data[2][1], data[3][0]]
            state = check_row([t1, t2])
            if ((state == 0)|(state == 1)):
                return "X won" if state == 0 else "O won"
            else:
                cum_states.append(state)
    if (cum_states == [2, 2, 2]):
        return "Draw"
    return "Game has not completed"

fid_ip = open('A-large.in', 'r')
fid_op = open('output.in', 'w')

num_cases = int(fid_ip.readline())

for case in range(0, num_cases):
    data = []
    for cnt in range(0, 4):
        data.append(list(fid_ip.readline().strip()))
    fid_op.write('Case #' + str(case+1) + ': ' + checker(data)+"\n")
    fid_ip.readline()
    

