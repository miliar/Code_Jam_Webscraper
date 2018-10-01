"""A
   Google CodeJam 2011
"""

from datetime import datetime


def routine(N, RP):
    pos = {'O':1, 'B':1}
    aim = {'O':None, 'B':None}
    moves = RP[:]
    
    s = 0
    #find initial aims
    for robot in pos:
        for i, rp in enumerate(RP):
            if rp[0] == robot:
                aim[robot] = i
                break
    
    while moves:
        move = moves.pop(0)
        
        while move:
            s += 1  #tick
            for robot in pos:
                if move and move[0] == robot:
                    if pos[robot] == move[1]:
                        move = None  #progressed
                        #find next aim
                        while aim[robot] < len(RP)-1:                            
                            aim[robot] += 1
                            if RP[aim[robot]][0] == robot:
                                break
                        else:
                            aim[robot] = None  #robot done
                        continue  #other robot could still move during this second
                if aim[robot] is not None:
                    if pos[robot] < RP[aim[robot]][1]:
                        pos[robot] += 1
                    elif pos[robot] > RP[aim[robot]][1]:
                        pos[robot] -= 1
                
        
    
    return s

if __name__ == '__main__':
    filename = "A-large"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        ins = f.readline().split()
        N = int(ins.pop(0))
        RP = []
        for i in xrange(N):
            R = ins.pop(0)
            P = int(ins.pop(0))
            RP.append((R,P))
        
        print N, RP

        print >>fo, "Case #%d: %s" % (case+1, routine(N, RP))

    fo.close()
    f.close()
    print datetime.now()
