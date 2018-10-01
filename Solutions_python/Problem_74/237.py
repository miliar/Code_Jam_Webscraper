#Codejam Problem A. Bot Trust
#Bots can move while the other has been doing nothing

from sys import stdin

cases = int(stdin.readline())

for caseNo in xrange(1, cases+1):
    lst = stdin.readline().split()
    no = int(lst[0])
    operations = []
    for i in xrange(no):
        at = 2*i + 1
        operations.append((int(lst[at] == 'O'), int(lst[at+1])))
    moment = 0
    pos = [1, 1]
    lastMove = [0, 0]
    for bot, at in operations:
        takes = max(0, abs(pos[bot] - at) - (moment - lastMove[bot])) + 1
        moment += takes
        pos[bot] = at
        lastMove[bot] = moment
    print "Case #%d: %d" % (caseNo, moment)

