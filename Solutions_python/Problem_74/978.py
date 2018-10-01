#!/usr/bin/python
import sys

debug = 0
def dp(s):
    if debug:
        print s

problem = sys.argv[0].split('.')[0]
datasize = sys.argv[1]
tryid = sys.argv[2]

ifh = open('%s-%s-%s.in' % (problem, datasize, tryid), 'rb')
ofh = open('%s-%s-%s.out' % (problem, datasize, tryid), 'wb')

testcases = int(ifh.readline())

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def findfirstmove(mlist, bot):
    for i, buttonpress in enumerate(mlist):
        if buttonpress[0] == bot:
            return i

def findnextmove(mlist, bot, lastmove):
    i = lastmove
    i += 1
    try:
        while (mlist[i][0] != bot):
            i += 1
    except IndexError:
        i = None
    return i

def whosnext(mptr):
    o = mptr['O']
    b = mptr['B']
    if o is None:
        o = 999
    if b is None:
        b = 999
    if o < b:
        return 'O'
    else:
        return 'B'

def otherbot(bot):
    if bot == 'O':
        return 'B'
    else:
        return 'O'

def movebot(move, loc):
    dp("moving %s from %d to %d" % (move[0], loc[move[0]], int(move[1])))
    vector = int(move[1]) - loc[move[0]]
    direction = vector / abs(vector)
    loc[move[0]] += direction

def process(moves):
    loc = { 'O' : 1,
            'B' : 1 }
    mptr = { 'O' : findfirstmove(moves, 'O'),
             'B' : findfirstmove(moves, 'B') }
    steps = 0
    curptr = 0
    while curptr < len(moves):
        curbot = whosnext(mptr)
        othbot = otherbot(curbot)
        dp("step %d - curbot %s othbot %s" % (steps, curbot, othbot))
        if (loc[curbot] == int(moves[curptr][1])):
            dp("%s is pushing button at %d" % (curbot, int(moves[curptr][1])))
            curptr += 1
            mptr[curbot] = findnextmove(moves, curbot, mptr[curbot]) # push button (aka find next move)
        else:
            movebot(moves[curptr], loc)
        if (mptr[othbot] is None):
            pass
        elif (loc[othbot] == int(moves[mptr[othbot]][1])):
            pass # wait for other bot to become current bot
        else:
            movebot(moves[mptr[othbot]], loc)
        steps += 1
    return "%d" % (steps,)

for case in range(1, int(testcases) + 1):
    rec = ifh.readline().split()
    buttoncount = int(rec.pop(0)) # strip off first field
    moves = list(chunks(rec, 2))
    ofh.write('Case #%d: %s\n' % (case, process(moves)))

ifh.close()
ofh.close()
