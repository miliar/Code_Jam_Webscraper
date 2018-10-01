def check(player, game_array):
    x_count = game_array[0].count(player)
    t_count = game_array[0].count('T')
    if x_count + t_count == 4:
        return True

    x_count = game_array[1].count(player)
    t_count = game_array[1].count('T')
    if x_count + t_count == 4:
        return True

    x_count = game_array[2].count(player)
    t_count = game_array[2].count('T')
    if x_count + t_count == 4:
        return True

    x_count = game_array[3].count(player)
    t_count = game_array[3].count('T')
    if x_count + t_count == 4:
        return True

    if (game_array[0][0] == player or game_array[0][0] == 'T') and (
                game_array[1][0] == player or game_array[1][0] == 'T') and (
                game_array[2][0] == player or game_array[2][0] == 'T') and (
                game_array[3][0] == player or game_array[3][0] == 'T'):
        return True

    if (game_array[0][1] == player or game_array[0][1] == 'T') and (
                game_array[1][1] == player or game_array[1][1] == 'T') and (
                game_array[2][1] == player or game_array[2][1] == 'T') and (
                game_array[3][1] == player or game_array[3][1] == 'T'):
        return True

    if (game_array[0][2] == player or game_array[0][2] == 'T') and (
                game_array[1][2] == player or game_array[1][2] == 'T') and (
                game_array[2][2] == player or game_array[2][2] == 'T') and (
                game_array[3][2] == player or game_array[3][2] == 'T'):
        return True

    if (game_array[0][3] == player or game_array[0][3] == 'T') and (
                game_array[1][3] == player or game_array[1][3] == 'T') and (
                game_array[2][3] == player or game_array[2][3] == 'T') and (
                game_array[3][3] == player or game_array[3][3] == 'T'):
        return True

    if (game_array[0][0] == player or game_array[0][0] == 'T') and (
                game_array[1][1] == player or game_array[1][1] == 'T') and (
                game_array[2][2] == player or game_array[2][2] == 'T') and (
                game_array[3][3] == player or game_array[3][3] == 'T'):
        return True

    if (game_array[0][3] == player or game_array[0][3] == 'T') and (
                game_array[1][2] == player or game_array[1][2] == 'T') and (
                game_array[2][1] == player or game_array[2][1] == 'T') and (
                game_array[3][0] == player or game_array[3][0] == 'T'):
        return True

    return False


def check_o(game_array):
    return False


f = open('input.txt', 'r')
test_cases = f.readline()
test_cases = int(test_cases.strip())
game_lines = 4

for i in range(0, test_cases, 1):
    game_array = []
    result = 'Game has not completed'
    for j in range(0, game_lines, 1):
        line = f.readline().strip()
        line = list(line)
        game_array.append(line)

    draw = True
    if '.' in game_array[0] or '.' in game_array[1] or '.' in game_array[2] or '.' in game_array[3]:
        draw = False

    if draw:
        result = 'Draw'

    win_x = check('X', game_array)
    if win_x:
        result = 'X won'
    else:
        win_o = check('O', game_array)
        if win_o:
            result = 'O won'

    f.readline()

    print 'Case #%d: %s' % (i + 1, result)