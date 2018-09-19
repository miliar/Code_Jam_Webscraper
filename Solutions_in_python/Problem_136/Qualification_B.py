filename = "B-small-attempt0"
#filename = "B-sample"
fi = open("C:\\Users\\Mike\\Downloads\\%s.in" % filename, "rb")
fo = open("%s.out" % filename, 'wb')

def read_int():
    return int(fi.readline().rstrip("\n"))

def read_int_array():
    a = []
    s = fi.readline().rstrip("\n").split(" ")
    for i in s:
        a.append(int(i))
    return a

def read_float_array():
    a = []
    s = fi.readline().rstrip("\n").split(" ")
    for i in s:
        a.append(float(i))
    return a

T = read_int()
for j in xrange(1, T+1):
    C, F, X = read_float_array()
    t1 = X / (2 + 0*F)
    M = 1
    while (True):
        t2 = X / (2 + M*F)
        for i in xrange(M):
            t2 += C / (2 + i*F)

        if t1 < t2:
            break;
        else:
            t1 = t2
            M += 1
    #print "Case #%d: %.7f" % (j, t1)
    fo.write("Case #%d: %.7f\n" % (j, t1))

    #t1 =                                 X / (2 + 0*F) # F multi on X is # of cookie houses
    #t2 =                 C / (2 + 0*F) + X / (2 + 1*F) # F multi on C is # of cookie houses-1 summed
    #t3 = C / (2 + 1*F) + C / (2 + 0*F) + X / (2 + 2*F)


fi.close()
fo.close()