def integize(char):
    if char is 'X':
        return 1
    elif char is 'O':
        return -1
    elif char is '.':
        return -10
    else:
        return 0

def fetch_input():
    is_dot_present = False
    input_line = raw_input().strip()
    if "." in input_line:
        is_dot_present = True
    input_string = []
    while input_line:
        input_string.append(input_line)
        input_line = raw_input().strip()
        if "." in input_line:
            is_dot_present = True
    return input_string,is_dot_present

input_list = []
input_line = raw_input()
N = int(input_line)
gameboard = []
gameboards = []
dot_map = {}
for i in xrange(N):
    (input_lines,is_dot_present) = fetch_input()
    dot_map[i] = is_dot_present
    gameboard = []
    for input_line in input_lines:
        input_list = map(integize,input_line)
        if input_list:
            gameboard.append(input_list)
    gameboards.append(gameboard)
results = []
ctr = 0
for gameboard in gameboards:
    row_total = [ sum(x) for x in gameboard ]
    col_total = [ sum(x) for x in zip(*gameboard) ]
    num_elmts = len(gameboard[0])
    leaddiag = [gameboard[i][i] for i in xrange(num_elmts)]
    traildiag = [gameboard[num_elmts-1-i][i] for i in xrange(num_elmts-1,-1,-1)]
    result = "Game has not completed"
    for total in row_total:
        if total >= 3:
            result = "X won"
    for total in row_total:
        if total in (-3,-4):
            if result is "X won":
                result = "Draw"
            else:
                result = "O won"
    for total in col_total:
        if total >= 3:
            if result is "O won":
                result = "Draw"
            elif result is not "Draw":
                result = "X won"
    for total in col_total:
        if total in (-3,-4):
            if result is "X won":
                result = "Draw"
            elif result is not "Draw":
                result = "O won"
    if sum(leaddiag) >= 3:
        if result is "O won":
            result = "Draw"
        elif result is not "Draw":
            result = "X won"

    if sum(leaddiag) in (-3,-4):
        if result is "X won":
            result = "Draw"
        elif result is not "Draw":
            result = "O won"

    if sum(traildiag) >= 3:
        if result is "O won":
            result = "Draw"
        elif result is not "Draw":
            result = "X won"
    
    if sum(traildiag) in (-3,-4):
        if result is "X won":
            result = "Draw"
        elif result is not "Draw":
            result = "O won"
    if result is "Game has not completed" and not dot_map[ctr]:
        result = "Draw"
    ctr += 1
    results.append(result)
case = 1
for result in results:
    display = "Case #"+str(case)+": "+result
    print display
    case += 1 
    
