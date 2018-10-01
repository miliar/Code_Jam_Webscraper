import itertools

with open("A-large.in", "rt") as infile:
    COUNT = int(infile.readline())

    X_WIN_SET = {'T', 'X'}
    O_WIN_SET = {'T', 'O'}

    for i in range(1, COUNT + 1):
        rows = list(itertools.islice((line.rstrip() for line in infile), 4))
        infile.readline()

        winner = None
        diagonal1 = set()
        diagonal2 = set()

        for j, row in enumerate(rows):
            diagonal1.add(row[j])
            diagonal2.add(row[-(j + 1)])

            if set(row) <= X_WIN_SET:
                winner = 'X'
                break
            if set(row) <= O_WIN_SET:
                winner = 'O'
                break

        if winner is None:
            for j, col in enumerate(zip(*rows)):
                if set(col) <= X_WIN_SET:
                    winner = 'X'
                    break
                if set(col) <= O_WIN_SET:
                    winner = 'O'
                    break

        if winner is None:
            if diagonal1 <= X_WIN_SET:
                winner = 'X'
            elif diagonal1 <= O_WIN_SET:
                winner = 'O'
            elif diagonal2 <= X_WIN_SET:
                winner = 'X'
            elif diagonal2 <= O_WIN_SET:
                winner = 'O'

        print("Case #%d: " % i, end="")
        if winner is None:
            if '.' in itertools.chain.from_iterable(rows):
                print("Game has not completed")
            else:
                print("Draw")
        else:
            print("%s won" % winner)
