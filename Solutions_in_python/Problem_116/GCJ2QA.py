for i in xrange(input()):
    B = ''.join([raw_input() for _ in xrange(4)])
    raw_input()
    print 'Case #%d:'%(i+1),
    if (   any(all(b in 'XT' for b in B[4*r:4*r+4]) for r in xrange(4))
        or any(all(b in 'XT' for b in B[c:16:4]) for c in xrange(4))
        or all(b in 'XT' for b in B[::5])
        or all(b in 'XT' for b in B[3:13:3])):
        print 'X won'
    elif (   any(all(b in 'OT' for b in B[4*r:4*r+4]) for r in xrange(4))
        or any(all(b in 'OT' for b in B[c:16:4]) for c in xrange(4))
        or all(b in 'OT' for b in B[::5])
        or all(b in 'OT' for b in B[3:13:3])):
        print 'O won'
    elif any(b=='.' for b in B):
        print 'Game has not completed'
    else:
        print 'Draw'
