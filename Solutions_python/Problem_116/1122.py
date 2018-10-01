from collections import defaultdict
inputfilename = 'test_iklklnpa.txt'

import sys
if len(sys.argv) > 1:
    inputfilename = sys.argv[1]

def get_freq(lst):
    freq = defaultdict(int)
    for el in lst:
        freq[el] +=1
    return freq

def check_win(lst):
    lstf = get_freq(lst)
    if lstf['T'] == 1: 
        if lstf['X'] == 3:
            return 'X'
        if lstf['O'] == 3:
            return 'O'
    else:
        if lstf['X'] == 4:
            return 'X'
        if lstf['O'] == 4:
            return 'O'        
def solve(lst):
    full = True
    winner = False
    for i in range(4):
        if '.' in lst[i]:
            full = False
        horizontal = lst[i]
        winner = check_win(horizontal)
        if winner: break
        winner = check_win([lst[el][i] for el in range(4)])
        if winner: break
    if winner:
        return '%s won' % winner
    left_diagonal = [lst[i][i] for i in range(4)]
    winner = check_win(left_diagonal)
    if winner:
        return '%s won' % winner
    right_diagonal = [lst[3-i][i] for i in range(4)]
    winner = check_win(right_diagonal)
    if winner:
        return '%s won' % winner
    if full:
        return 'Draw'
        
    return 'Game has not completed'


with open(inputfilename) as fp:
    N = int(fp.readline())
    for pr in range(N):
        problem = []
        for i in range(4):
            problem.append(list(fp.readline().strip()))
        #print problem
        print "Case #%s: %s" %(pr+1, solve(problem))
        fp.readline()