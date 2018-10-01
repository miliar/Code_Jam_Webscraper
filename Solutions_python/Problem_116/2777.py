#!/usr/bin/env python
# -*- utf-8 -*-

def line_gen(l):
    yield l[0:4]
    yield l[4:8]
    yield l[8:12]
    yield l[12:16]
    # yield "----"
    yield l[0:13:4]
    yield l[1:14:4]
    yield l[2:15:4]
    yield l[3:16:4]
    # yield "===="
    yield l[0:16:5]
    yield l[3:13:3]

def checker(l):
    Xs = 0
    Os = 0
    Ts = 0
    Ds = 0
    for c in l:
        if c == '.':
            return (False, '.')
        elif c == 'X':
            if Os > 0:
                return (False, '')
            else:
                Xs += 1
        elif c == 'O':
            if Xs > 0:
                return (False, '')
            else:
                Os += 1
        elif c == 'T':
            Ts += 1

    # print Xs,Os,Ts

    if (Xs == 3 and Ts == 1) or Xs == 4:
        return (True, 'X')
    elif (Os == 3 and Ts == 1) or Os == 4:
        return (True, 'O')

def main():
    f = open("A-small-attempt0.in", "r")
    num = int(f.readline())
    for i in range(0,num):
        l = ""
        # read four lines
        l += f.readline().strip()
        l += f.readline().strip()
        l += f.readline().strip()
        l += f.readline().strip()

        bContainDot = False
        winner = ''
        for candi in line_gen(l):
            bR, r = checker(candi)
            # print l
            # print bR,r
            if bR == False and r == '.':
                bContainDot = True
            elif bR:
                # print "Case #%d: %c won" % (i+1, r)
                winner = r
                break
        if winner:
            print "Case #%d: %c won" % (i+1, winner)
        elif bContainDot:
            print "Case #%d: Game has not completed" % (i+1)
        else:
            print "Case #%d: Draw" % (i+1)
            
        # skip empty line
        f.readline()

    # close file
    f.close()

if __name__ == "__main__":
    main()
    # print checker("OOOO")
    # print checker("XXXX")
    # print checker("XXTX")
    # print checker("OOTO")
    # print checker("....")
    # print checker("O..T")
    # print checker("OOXX")
