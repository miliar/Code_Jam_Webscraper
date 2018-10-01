#!python3
f = open("A-small-attempt1.in", 'r')
g = open("out.txt", 'w')

stuff = f.read()
f.close()

L = stuff.split("\n")
cases = int(L.pop(0))

def rows(board):
    value = ""
    
    for i in board:
        if "." in i:
            continue
        value = i[0]
        if value == "T":
            value = i[1]
            
        for j in i:
            if j == "T":
                continue
            elif not value == j:
                break
        else:
            return (True, value)
    return (False, None)

def cols(board):
    value = ""
    for i in range(4):
        value = board[0][i]
        if value == ".":
            continue
        elif value == "T":
            value = board[1][i]
        for j in range(4):
            if board[j][i] == "T":
                continue
            elif board[j][i] == ".":
                break
            elif not value == board[j][i]:
                break
        else:
            return (True, value)
    return (False, None)

def posDiag(board):
    value = board[0][0]
    if value == ".":
        return (False, None)
    elif value == "T":
        value = board[1][1]

    for i in range(4):
        if board[i][i] == "T":
            continue
        elif not value == board[i][i]:
            return (False, None)
    else:
        return (True, value)


def negDiag(board):
    value = board[0][-1]
    if value == ".":
        return (False, None)
    elif value == "T":
        value = board[1][-2]

    for i in range(4):
        if board[i][-(i+1)] == "T":
            continue
        elif not value == board[i][-(i+1)]:
            return (False, None)
    else:
        return (True, value)

def draw(board):
    for i in board:
        for j in i:
            if j == ".":
                return False
    return True

for case in range(cases):
    
    board = []
    for i in range(4):
        board.append(list(L.pop(0)))
    L.pop(0)

    if rows(board)[0]:
        winner = rows(board)[1]
        answer = "{} won".format(winner)
    elif cols(board)[0]:
        winner = cols(board)[1]
        answer = "{} won".format(winner)
    elif negDiag(board)[0]:
        winner = negDiag(board)[1]
        answer = "{} won".format(winner)
    elif posDiag(board)[0]:
        winner = posDiag(board)[1]
        answer = "{} won".format(winner)
    elif draw(board):
        answer = "Draw"
    else:
        answer = "Game has not completed"
        

    g.write("Case #{}: {}\n".format(case+1, answer))
g.close()
