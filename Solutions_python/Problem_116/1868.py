def get_game():
    game = []
    for i in range(4):
        game += list(raw_input().strip())
    raw_input()
    return game


def did_won(who):
    rows = [0, 0, 0, 0]
    columns = [0, 0, 0, 0]
    diags = [0, 0]
    for idx, field in enumerate(game):
        if (field == who or field == 'T'):
            row = idx / 4
            rows[row] += 1
            
            col = idx % 4
            columns[col] += 1
            
            if col == row:
                diags[0] += 1
            elif (col + row == 3):
                diags[1] += 1
                
    if (4 in  diags) or (4 in rows) or (4 in columns):
        return True
    else:
        return False
                
def has_empty_fields(game):
    for field in game:
        if field == ".":
            return True
    return False

def solve_game(game):
    x_won = did_won('X')
    o_won = did_won('O')
    
    if x_won and o_won:
        return "Draw"
    elif x_won:
        return "X won"
    elif o_won:
        return "O won"
    
    if has_empty_fields(game):
        return "Game has not completed"
    else: 
        return "Draw"

count = int(raw_input().strip())

for i in range(count):
    game = get_game()
    print "Case #{0}: {1}".format(i + 1, solve_game(game))
