import sys

def do_test_case(fd):
    blocks = int(fd.readline())

    nao = [float(x) for x in fd.readline().split()]
    ken = [float(x) for x in fd.readline().split()]

    # war
    ns = sorted(nao)
    ks = sorted(ken)
    war = 0

    for nb in ns:
        if nb > ks[-1]:
            ks.remove(ks[0])
            war += 1
        else:
            for kb in ks:
                if nb < kb:
                    ks.remove(kb)
                    break;

    # d-war
    dwar = 0
    ks = sorted(ken)

    while ns:
        if ns[-1] > ks[-1]:
            dwar += 1
            ns.remove(ns[-1])
            ks.remove(ks[-1])
        else:
            ns.remove(ns[0])
            ks.remove(ks[-1])


    return (dwar, war)


##################
file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    (y,z) = do_test_case(fd)
    print "Case #%d: %d %d" % (i,y,z)

