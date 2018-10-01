def same(who, tile):
    return who == tile or tile == 'T'
    
T = input()
for case in xrange(1, T+1):
    tile = []
    tile.append([c for c in raw_input()])
    tile.append([c for c in raw_input()])
    tile.append([c for c in raw_input()])
    tile.append([c for c in raw_input()])
        
    is_draw = True
    for t in tile:
        if '.' in t:
            is_draw = False
    message = 'Game has not completed'
    if is_draw:
        message = 'Draw'
    game = True
    
    for c in 'OX':
        if game:
            for i in range(4):
                win = False
                
                for j in range(4):
                    if not same(c, tile[i][j]):
                        break
                    elif j == 3:
                        win = True
                if not win:
                    for j in range(4):
                        if not same(c, tile[j][i]):
                            break                         
                        elif j == 3:
                            win = True
                if not win:            
                    for j in range(4):
                        if not same(c, tile[j][j]):
                            break
                        elif j == 3:
                            win = True
                if not win:
                    for j in range(4):
                        if not same(c, tile[3-j][j]):
                            break                         
                        elif j == 3:
                            win = True
                if win:
                    message = '%s won' % c
                    game = False
                    break
    raw_input()
    print 'Case #{}: {}'.format(case, message)