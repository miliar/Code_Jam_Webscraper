def digits(num):
    ret = []
    while num > 0:
        ret.insert(0, num %10)
        num /= 10
        
    return ret

def is_tidy(seq):
    if len(seq) == 0:
        return True

    a = seq[0]
    for i in xrange(1, len(seq)):
        if seq[i] < a:
            return False
        a = seq[i]

    return True

def one_pass(digs, index):
#    print digs
    
    if digs[index] >= digs[index - 1]:
        return

    for i in xrange(index, len(digs)):
        digs[i] = 9
        
    digs[index - 1] = digs[index - 1] - 1

def solve(N):
    digs = digits(N)

    for i in xrange(len(digs)-1, 0, -1):
        for j in xrange(len(digs)-1, 0, -1):
            one_pass(digs, j)
    return int(''.join([str(dig) for dig in digs]))

T = int(raw_input())

for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve(int(raw_input())))

    
