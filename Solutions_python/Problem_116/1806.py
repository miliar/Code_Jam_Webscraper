import os

WIN_LIST = [set('O'), set('X'), set(('O', 'T')), set(('X', 'T'))]

def setter(input=None):
    """ Read input file and return case in order
    
    """
    cases = int(input.readline())
    
    for case in xrange(cases):
        row = []
        for r in xrange(4):
            row.append(input.readline().rstrip('\n'))
        input.readline()
        yield case+1, row

def inset(set_now, target):
    if set_now in target:
        set_now.discard('T')
        return True
    return False

def isfull(map):
    for i in xrange(4):
        for j in xrange(4):
            if map[i][j] == '.':
                return False
    return True
    
    
os.chdir(r'D:\ypsun\codejam\2013\Qualification Round\A. Tic-Tac-Toe-Tomek')
job = 'A-large'

input = open(job+'.in', 'r')
output = open(job+'.out', 'w')

for case, row in setter(input):
    # Game has not completed
    result = 'Game has not completed'
    # won: diagonal
    set_list = []
    set_list.append(set('%s%s%s%s' % (row[0][0], row[1][1], row[2][2], row[3][3])))  # diagonal 1
    set_list.append(set('%s%s%s%s' % (row[0][3], row[1][2], row[2][1], row[3][0])))  # diagonal 2
    for set_now in set_list:
        if inset(set_now, WIN_LIST):
            result = set_now.pop() + ' won'
            break
    # won: row or column
    if result == 'Game has not completed':
        set_list = []
        for k in xrange(4):
            set_list.append(set('%s%s%s%s' % (row[k][0], row[k][1], row[k][2], row[k][3])))  # row k
            set_list.append(set('%s%s%s%s' % (row[0][k], row[1][k], row[2][k], row[3][k])))  # column k
        for set_now in set_list:
            if inset(set_now, WIN_LIST):
                result = set_now.pop() + ' won'
                break
    # Draw
    if result == 'Game has not completed':
        if isfull(row):
            result = 'Draw'

    output.write('Case #%s: %s\n' % (case, result))
        
input.close()
output.close()