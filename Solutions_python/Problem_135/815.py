def card_trick (A, B, i, j):
    '''A is the first arrangement of cards (a list); B is the second
       arrangement of cards; i is the row picked in A; j is the row picked
       in B'''
    row1, row2 = A[i - 1], B[j - 1]
    common = set(row1).intersection(set(row2))
    l = len(common)
    if l == 0:
        return 'Volunteer cheated!'
    elif l == 1:
        elem = common.pop()
        return str(elem)
    else:
        return 'Bad magician!'
    



f = open('cardtrickIN.in', 'r')
g = open('cardtrickOUT.txt', 'w')
numCases = int(f.readline())
for case in xrange(1, numCases + 1):
    first_answer = int(f.readline())
    first_arrangement = []
    for _ in xrange (4):
        line = f.readline().split()
        row = map(lambda x: int(x), line)
        first_arrangement.append(row)
    second_answer = int(f.readline())
    second_arrangement = []
    for _ in xrange (4):
        line = f.readline().split()
        row = map(lambda x: int(x), line)
        second_arrangement.append(row)
    g.write ('Case #' + str(case) + ': ' + card_trick (first_arrangement,\
                                                       second_arrangement,\
                                                       first_answer,\
                                                       second_answer) + '\n')
g.close()
f.close()
        