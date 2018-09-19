
"""
    This program is written by kawasaki, Japan.
    
    mail: kawasaki.yasuhiro@gmail.com
    twitter: http://twitter.com/pheromo/
    blog: http://d.hatena.ne.jp/phero/
    
    copyright 2010 kawasaki.
"""

#DEBUG = True
DEBUG = False

import sys

if DEBUG:
    input_data = [
        '4',
        '7 3',
        '.......',
        '.......',
        '.......',
        '...R...',
        '...BB..',
        '..BRB..',
        '.RRBR..',
        '6 4',
        '......',
        '......',
        '.R...R',
        '.R..BB',
        '.R.RBR',
        'RB.BBB',
        '4 4',
        'R...',
        'BR..',
        'BR..',
        'BR..',
        '3 3',
        'B..',
        'RB.',
        'RB.',
    ]
else:
    input_data = []
    for line in sys.stdin:
        while line[-1] in ['\r', '\n']:
            line = line[:-1]
        input_data.append(line)

line_id = 0
def readline():
    global line_id
    line_id += 1
    return input_data[line_id - 1]

if DEBUG:
    import time
    _START_TIME = time.time()

#-------------------------------------------------------------------------------
#   Algorithm.

T = int(readline())

BLANK, R, B = 0, 1, 2

qid = 1
while qid <= T:
    
    N, K = map(int, readline().split(' '))
    brd = []
    for i in xrange(N):
        conv = lambda x: {'.':BLANK, 'R':R, 'B':B}[x]
        line = [conv(c) for c in readline()]
        brd.append(line)
    
#    def rotate(brd):
#        new_brd = [[BLANK for col in row] for row in brd]
#        for row_id, row in enumerate(brd):
#            for col_id, col in enumerate(row):
#                new_brd[col_id][N - 1 - row_id] = col
#        return new_brd
    
    def gravity_to_right(brd):
        new_brd = []
        for row in brd:
            new_row = [BLANK] * N
            current_pos = N - 1
            for pos in xrange(N - 1, -1, -1):
                if row[pos] != BLANK:
                    new_row[current_pos] = row[pos]
                    current_pos -= 1
            new_brd.append(new_row)
        return new_brd
    
    def find_line(brd):
        found = {
            R:False,
            B:False,
            BLANK:True,
        }
        for y in xrange(N):
            for x in xrange(N):
                target = brd[y][x]
                if found[target]:
                    continue
                
                for dx, dy in ((1, 0), (-1, 1), (0, 1), (1, 1)):
                    line_found = True
                    for i in xrange(1, K):
                        tx = x + dx * i
                        ty = y + dy * i
                        if tx < 0 or N <= tx or ty < 0 or N <= ty:
                            line_found = False
                            break
                        else:
                            if brd[ty][tx] != target:
                                line_found = False
                                break
                    if line_found:
                        found[target] = True
        if found[R]:
            if found[B]:
                return 'Both'
            return 'Red'
        if found[B]:
            return 'Blue'
        return 'Neither'
    
    print 'Case #%d: %s' % (qid, find_line(gravity_to_right(brd)))
    
    qid += 1

#---------------------------------------------------------------------------

if DEBUG:
    print '-' * 80
    print 'DEBUG version finished. %.3f [sec]' % (time.time() - _START_TIME)

