import sys, StringIO

DEBUG = 0

U = [('R', [2,4,3]),  # 0th. color is R, should follow one of the idx colors
     ('O', [4]),
     ('Y', [0,4,5]),
     ('G', [0]),
     ('B', [2,0,1]),
     ('V', [2])
     ]
RESULT = None

def nextStep(c1, s1, x):
    global RESULT
    c = c1[:]
    s = s1[:]
    c[x]-=1
    s.append(x)

    if sum(c)==0:
        #Check if first and last are valid:
        if s[-1] in U[s[0]][1]:
            if DEBUG: print "############ %s  " % s
            RESULT = s
        else:
            if DEBUG: print "END - not valid: %s" % s
        return

    #choose the biggest (of the possible) - non-recursive
    while max(c)>5:
        possible = U[s[-1]][1]
        idx = 0
        for i in range(len(possible)):
            if c[possible[i]]>c[possible[idx]]:
                idx = i
        c[possible[idx]]-=1
        s.append(possible[idx])

    #below 5 - try all resursive
    possible = U[s[-1]][1]
    for i in range(len(possible)):
        if c[possible[i]]>0  and not RESULT:
            #print "%s -> %s" % (c, s)
            #if DEBUG: print "   choose %d" % possible[i]
            nextStep(c, s, possible[i])

def solution(d, c, s):
    global RESULT
    RESULT = None
    #choose the biggest number odd number
    for i in range(len(c)):
        if c[i]>0  and not RESULT:
            #if DEBUG: print "   choose %d" % i
            nextStep(c, s, i)
    if RESULT:
        return "".join(map(lambda x: U[x][0], RESULT))
    return "IMPOSSIBLE"
#solution


if __name__ == '__main__':
    if len(sys.argv)>1:
        input = file(sys.argv[1])
    else:
        input = StringIO.StringIO("""5
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2
101 50 1 50 0 0 0
""")
    cases = int(input.readline())
    for case in range(cases):
        c = map(int, input.readline().split())
        n = c.pop(0)
        print("Case #%d: %s" % (case+1, solution(n, c, [])))