def game_state(game):
    '''
    Compute the game state.

    @return: (str).
    '''
    has_empty = False
    dot = '.'

    # check if X or O won
    for symbol in ('X', 'O'):
        map_fct = lambda item: True if item == symbol or item == 'T' else False

        # check rows
        for row in xrange(4):
            if all(map(map_fct, game[row][:])):
                return '%s won' % symbol
            if dot in game[row]:
                has_empty = True
        # check columns
        for col in xrange(4):
            if all(map(map_fct, [l[col] for l in game])):
                return '%s won' % symbol

        # check diagonals
        diag = []
        for i in xrange(4):
            # 0,3  1,2  2,1  3,0
            diag.append(game[i][3 - i])
        if all(map(map_fct, diag)):
            return '%s won' % symbol

        diag = []
        for i in xrange(4):
            # 0,0  1,1  2,2  3,3
            diag.append(game[i][i])
        if all(map(map_fct, diag)):
            return '%s won' % symbol

    if has_empty:
        return 'Game has not completed'
    return 'Draw'


if __name__ == '__main__':
    input_file = open('A-large.in', 'r')
    output_file = open('A-large.out', 'w')

    test_cases_count = int(input_file.readline())

    for line_number in range(test_cases_count):
        game = [[None, None, None, None] for _ in xrange(4)]

        # read in game state
        for i in xrange(4):
            line = input_file.readline().strip()
            for j in xrange(4):
                game[i][j] = line[j]
        # read the empty line
        input_file.readline()

        output_file.write('Case #%d: %s\n' % \
                          (line_number + 1, game_state(game)))

    input_file.close()
    output_file.close()
