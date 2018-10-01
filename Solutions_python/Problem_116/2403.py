import sys

winning_masks = [
                    "1111000000000000",
                    "0000111100000000",
                    "0000000011110000",
                    "0000000000001111",
                    "1000010000100001",
                    "0001001001001000",
                    "1000100010001000",
                    "0100010001000100",
                    "0010001000100010",
                    "0001000100010001",
                 ]

if sys.argv < 2:
    print 'Missing file argument'
    sys.exit(1)

with open(sys.argv[1]) as fh:
    lines = fh.readlines()[1:]

    game_idx = 1
    game = [] 
    for line in lines: 
        line = line.strip()

        if line != '':
            game.append(line)

        if len(game) == 4: 
            print 'Case #%d: ' % (game_idx,),
            game_idx += 1
            game_con = ''.join(game)
            game = []

            done = False
            for mask in winning_masks:
                pattern = []

                for idx in xrange(len(game_con)):
                    if len(pattern) == 4:
                        break
                    state = game_con[idx]
                    if mask[idx] == '1':
                        pattern.append(state)

                if 'O' in pattern and not 'X' in pattern and not '.' in pattern:
                    print 'O won'
                    done = True
                    break
                if 'X' in pattern and not 'O' in pattern and not '.' in pattern:
                    print 'X won'
                    done = True
                    break

            if done:
                continue

            if '.' in game_con: 
                print 'Game has not completed'
            else:
                print 'Draw'
