import sys, os, math

def gentupl(total, p, sleft):
    #Return (a, b, c, is_ok, avrg, is_sup, reason)
    print (total, p, sleft)
    avrg = total / 3.0
    if p <= avrg:
        return (-1, -1, -1, True, avrg, False, 'Average > P')
    b = int(math.floor(avrg))
    if p - b > 2:
        return (-1, b, -1, False, avrg, False, 'P is too large')
    a = b
    c = total - a - b
    if math.fabs(a - c) <= 1 and p <= max(a,b,c) and min(a,b,c) > 0:
        return (a, b, c, True, avrg, False, 'OK')
    a = b + 1
    c = total - a - b
    if math.fabs(a - c) <= 1 and p <= max(a,b,c) and min(a,b,c) > 0:
        return (a, b, c, True, avrg, False, 'OK')
    if sleft > 0:
        for a in range(b-1, b+3):
            c = total - a - b
            if math.fabs(a - c) <= 2 and p <= max(a,b,c) and min(a,b,c) > 0:
                return (a, b, c, True, avrg, True, 'OK')
    return (a, b, c, False, avrg, False, 'No more suprise')
        
if len(sys.argv) > 1:
    f = open(sys.argv[1], 'r')
    fo = open(sys.argv[1] + '.out', 'w')


    cno = int(f.readline())
    print cno

    for c in range(1,cno+1):
        line = f.readline()
        args = line.split(' ')
        glerno = int(args[0])
        s = int(args[1])
        p = int(args[2])
        passno = 0
        for i in range(3, 3+glerno):
            tpl = gentupl(int(args[i]), p, s)
            print tpl
            if tpl[3]:
                passno += 1
                if tpl[5]:
                    s -= 1
        print passno
        if c != 1:
            fo.write("\n" + 'Case #'+str(c)+': ' + str(passno))
        else:
            fo.write('Case #'+str(c)+': ' + str(passno))
    f.close()
    fo.close()
