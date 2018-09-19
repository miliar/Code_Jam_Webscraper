f = open("A-large.in", "r").readlines()
output = open("out.txt", "w")

num_inputs = int(f[0])

counter = 0
for x in range(1, num_inputs * 5, 5):
    counter += 1
    board = []
    for i in range(4):
        board.append(f[x + i][:-1])

    winner = ""
    print(board)

    for p in ["X", "O"]:
        valid = lambda x: x == p or x == "T"

        # Check rows
        for row in board:
            if all(map(valid, row)):
                if not winner:
                    winner = p

        # check columns
        works = False
        for i in range(4):
            cols = [y[i] for y in board]
            if all(map(valid, cols)):
                works = True
                break


        if works and not winner:
            winner = p

        # Diaganals
        board[0][0], board[1][1]
        if all(map(valid, [board[a][3-(3-a)] for a in range(4)])):
            if not winner:
                winner = p

        if all(map(valid, [board[a][3-a] for a in range(4)])):
            if not winner:
                winner = p

    output.write("Case #%d: " % (counter))
    if not winner:
        full = True
        for row in board:
            if "." in row:
                full = False
                break

        if full:
            output.write("Draw\n")
        else:
            output.write("Game has not completed\n")
    else:
        output.write("%s won\n" % (winner.upper()))


