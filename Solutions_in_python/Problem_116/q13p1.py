#6:20pm
test_case = \
'''\
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
'''

test_solution = \
'''\
Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
'''

from collections import Counter, defaultdict
from operator import itemgetter

class Solver:

    def __init__(self, reader):
        self.reader = reader
        self.lines = []
        # rows
        self.lines += [[(x, y) for y in range(4)] for x in range(4)]
        # cols
        self.lines += [[(x, y) for x in range(4)] for y in range(4)]
        # main diag
        self.lines += [[(x, x) for x in range(4)]]
        # opp diag
        self.lines += [[(x, 3-x) for x in range(4)]]
        
    def solve(self):
        board = []
        t_pos = None
        board_full = True
        for i in range(4):
            row = self.reader.get_list(types=str, sep='')
            try:
                t_pos = (i, row.index('T'))
            except ValueError:
                pass
            if '.' in row:
                board_full = False
            board.append(row)
        try:
            self.reader.get_line()
        except StopIteration:
            pass

        for player in ('X', 'O'):
            goal = [player] * 4
            if t_pos is not None:
                board[t_pos[0]][t_pos[1]] = player
            for line in self.lines:
                if [board[p[0]][p[1]] for p in line]  == goal:
                    return player + ' won'
        if board_full:
            return 'Draw'
        else:
            return 'Game has not completed'
        
            
        #word = self.reader.get_value(type_ = str)
        #counter = Counter(word)
        #base = max(len(counter), 2)
        #word_length = len(word)
        #tr = {}
        #i = 0
        #pos_values = [1]
        #for k in range(word_length-1):
            #pos_values.append(pos_values[-1]*base)
        #value = 0
        #for k, char in enumerate(word):
            #if char not in tr:
                #if i == 0:
                    #digit = 1
                #elif i == 1:
                    #digit = 0
                #else:
                    #digit = i
                #tr[char] = digit
                #i += 1
            #else:
                #digit = tr[char]
            #value += pos_values[word_length-k-1] * digit
            
        #print(word)
        #print(base)
        #print(tr)
        #return value
            
    
