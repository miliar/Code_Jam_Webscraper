import sys

def nextTarget(col):
    for t in todo:
        if t[0] == col:
            return t[1]
    return 0

with open(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for i in range(T):
        todo = []
        line = iter(f.readline().strip().split())
        N = int(line.next())
        for n in range(N):
            todo.append((line.next(), int(line.next())))
        
        time = 0
        bPos = 1
        oPos = 1
        bTarget = nextTarget('B')
        oTarget = nextTarget('O')
        while todo:
            press = False
            if todo[0][0] == 'B' and bPos == todo[0][1]:
                press = True
            elif bTarget > bPos:
                bPos += 1
            elif bTarget < bPos:
                bPos -= 1
            if todo[0][0] == 'O' and oPos == todo[0][1]:
                press = True
                oTarget = nextTarget('O')
            elif oTarget > oPos:
                oPos += 1
            elif oTarget < oPos:
                oPos -= 1
            if press:
                todo.pop(0)
                bTarget = nextTarget('B')
                oTarget = nextTarget('O')
            time += 1
        print "Case #%d:" % (i+1), time        
