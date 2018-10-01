fname = 'A-large.in'
with open(fname) as f:
    content = f.readlines()

total = int(content.pop(0))

case = 0

def get_value(matrix, x, y, previous=None):
    if(matrix[x][y]=='T'):
        return previous
    if(matrix[x][y]=='.'):
        return False

    if(previous==None):
        return matrix[x][y]

    return previous if previous == matrix[x][y] else False

while(case < total):
    case+=1
    tic_game = content[(case-1)*5:(case-1)*5+4]
    tic_game = [list(x.strip()) for x in tic_game]

    result = get_value(tic_game, 0, 0, get_value(tic_game, 1, 1, get_value(tic_game, 2, 2, get_value(tic_game, 3, 3))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 3, 0, get_value(tic_game, 2, 1, get_value(tic_game, 1, 2, get_value(tic_game, 0, 3))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 0, 0, get_value(tic_game, 0, 1, get_value(tic_game, 0, 2, get_value(tic_game, 0, 3))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 1, 0, get_value(tic_game, 1, 1, get_value(tic_game, 1, 2, get_value(tic_game, 1, 3))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 2, 0, get_value(tic_game, 2, 1, get_value(tic_game, 2, 2, get_value(tic_game, 2, 3))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 3, 0, get_value(tic_game, 3, 1, get_value(tic_game, 3, 2, get_value(tic_game, 3, 3))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 0, 0, get_value(tic_game, 1, 0, get_value(tic_game, 2, 0, get_value(tic_game, 3, 0))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 0, 1, get_value(tic_game, 1, 1, get_value(tic_game, 2, 1, get_value(tic_game, 3, 1))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 0, 2, get_value(tic_game, 1, 2, get_value(tic_game, 2, 2, get_value(tic_game, 3, 2))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue
    
    result = get_value(tic_game, 0, 3, get_value(tic_game, 1, 3, get_value(tic_game, 2, 3, get_value(tic_game, 3, 3))))
    if(result):
        print 'Case #%d: %s won' % (case, result)
        continue

    draw = ''.join([ str(''.join(str(i) for i in x)) for x in tic_game ]).find('.')
    print 'Case #%d: Draw' % case if draw == -1 else 'Case #%d: Game has not completed' % case
