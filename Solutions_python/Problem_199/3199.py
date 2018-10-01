import logging

logging.basicConfig(format='%(message)s')

def decode(s):
    v = 0
    for i, c in enumerate(s):
        if c == '-': v += (1 << (len(s) - i - 1))

    n = len(s)

    return v, n

def encode(v, n):
    s = ''
    for i in range(n):
        if v & (1 << (n - i-1)): s += "-"
        else:  s += "+"

    return s

def flip(v, n, to_flip, at):
    return v ^ ((2**to_flip -1) << (n - at-1))

def recurse(flips, v, n, K):
    #print encode(v, n)
    some_missing = False
    count = flips[v]
    for i in xrange(K-1, n):
        v_next = flip(v, n, K, i)
        #if (v_next == 0): print 'SOLVED!'
        if v_next not in flips:
            flips[v_next] = count + 1
            some_missing = True
        elif flips[v_next] > count+1:
            flips[v_next] = count+1

        if some_missing and (v_next != 0): recurse(flips, v_next, n, K)

def do_case(S, K):
    v, n = decode(S)
    flips = {}

    flips[v] = 0

    recurse(flips, v, n, K)
    #print flips
    if 0 in flips:
        return "%d" % flips[0]
    else:
        return "IMPOSSIBLE"

# main starts here

T = int(raw_input())

for i in xrange(T):
    line = raw_input()
    S, K = line.split()
    K = int(K)

    soln = do_case(S, K)

    print("Case #%d: %s" % (i+1, soln))
    logging.warn("Case #%d: %s" % (i+1, soln))

