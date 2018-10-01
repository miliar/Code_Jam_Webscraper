import fileinput

infile = fileinput.input()

def r(fn='none', splt=True):
    '''r(fn=none, splt=True)
    Example: N, = r(long)
    S = r(str,splt=False)
    '''
    inp = infile.readline()
    if splt:
        inp = inp.split()
        return map(fn, inp)
    else:
        return fn(inp)

T, = r(long)

for t in range(T):
    D = r(int)
    N = D.pop(0)
    S = D.pop(0)
    p = D.pop(0)
    m = p*3
    max = 0
    surprise = 0

    for score in D:
        diff = score - m
        #print diff
        if diff >= -4 and (score - p)/2 >= 0:
            max += 1
            if diff < -2:
                surprise += 1
    if surprise > S:
        #print surprise,S,max
        max = max - (surprise - S)
    print "Case #%d: %d"%(t+1, max)
