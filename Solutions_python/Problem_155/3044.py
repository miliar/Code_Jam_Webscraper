import sys

cases = int(sys.stdin.readline())

for idxCase in xrange(cases):
    sMax, shyness = sys.stdin.readline().split(' ')
    standUp = 0
    friends = 0

    for levelShyness, persons in enumerate(shyness):
        if levelShyness > int(sMax):
            break
        friend = max(0, levelShyness - standUp)
        friends += friend
        standUp += friend + int(persons)

    print 'Case #%d: %d' % (idxCase + 1, friends)
