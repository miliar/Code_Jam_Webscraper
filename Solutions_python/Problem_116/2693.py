__author__ = 'Bassut'

n = raw_input()
n = int(n)
z = n
cases = []
while z > 0:
    row1 = raw_input()
    if row1 == '':
        row1 = raw_input()
    row2 = raw_input()
    row3 = raw_input()
    row4 = raw_input()

    cases.append((row1, row2, row3, row4))
    z -= 1

def check2(a, b, c, d, t, game):
    d = [game[a[0]][a[1]], game[b[0]][b[1]], game[c[0]][c[1]], game[d[0]][d[1]]]
    letter, dot = 0, 0
    for each in d:
        if each == t:
            letter += 1
        if each == '.':
            dot += 1

    return [letter, dot]

def check(a, b, c, d, t, game):
    d = [game[a[0]][a[1]], game[b[0]][b[1]], game[c[0]][c[1]], game[d[0]][d[1]]]
    to_check = [t, 'T']
    if d[0] in to_check and d[1] in to_check and d[2] in to_check and d[3] in to_check:
        return 4
    if d[0] == t and d[1] == t and d[2] == t:
        return 3
    if d[1] == t and d[2] == t and d[3] == t:
        return 3
    else:
        return '-'

def is_over(game):
    for i in range(4):
        a = check2((i, 0), (i, 1), (i, 2), (i, 3), 'X', game)
        if a[0] != 4 and a[1] > 0:
            return False
        a = check2((i, 0), (i, 1), (i, 2), (i, 3), 'O', game)
        if a[0] != 4 and a[1] > 0:
            return False
        a = check2((0, i), (1, i), (2, i), (3, i), 'X', game)
        if a[0] != 4 and a[1] > 0:
            return False
        a = check2((0, i), (1, i), (2, i), (3, i), 'O', game)
        if a[0] != 4 and a[1] > 0:
            return False

    return True

for loop in range(n):
    game = cases[loop]
    X = None
    O = None
    result = ()
    cur_score = []
    for i in range(4):
        cur_score = []
        # vertically
        a = check((i, 0), (i, 1), (i, 2), (i, 3), 'X', game)
        if a != '-':
            X = a

        # vertically
        a = check((i, 0), (i, 1), (i, 2), (i, 3), 'O', game)
        if a != '-':
            O = a

        # horizontally
        a = check((0, i), (1, i), (2, i), (3, i), 'X', game)
        if a != '-':
            if a > X:
                X = a

        # horizontally
        a = check((0, i), (1, i), (2, i), (3, i), 'O', game)
        if a != '-':
            if a > O:
                O = a

        # diagonally
        a = check((0, 0), (1, 1), (2, 2), (3, 3), 'X', game)
        if a != '-':
            if a > X:
                X = a

        # diagonally
        a = check((0, 3), (1, 2), (2, 1), (3, 0), 'X', game)
        if a != '-':
            if a > X:
                X = a

        # diagonally
        a = check((0, 0), (1, 1), (2, 2), (3, 3), 'O', game)
        if a != '-':
            if a > O:
                O = a

        # diagonally
        a = check((0, 3), (1, 2), (2, 1), (3, 0), 'O', game)
        if a != '-':
            if a > O:
                O = a

        if not cur_score:
            cur_score = (X, O)
        elif cur_score[0] > X:
            cur_score[0] = X
        elif cur_score[1] > O:
            cur_score[1] = O

    result = result + (cur_score,)

    for each in result:
        if each[0] == 4:
            print 'Case #%d: X won' % (loop + 1)
        elif each[1] == 4:
            print 'Case #%d: O won' % (loop + 1)
        elif each[0] != each[1]:
            print 'Case #%d: %s won' % (loop + 1, 'O' if each[1] > each[0] else 'X')
        elif each[0] == each[1] and is_over(game):
            print 'Case #%d: Draw' % (loop + 1)
        elif not is_over(game):
            print 'Case #%d: Game has not completed' % (loop + 1)