import sys

def tic(ten):
    full = 1
    result = 0

    for matrix in ten:
        if full == 1:
            if matrix['.'] > 0:
                full = 0

        if matrix['X'] == 4 or (matrix['X'] + matrix['T'] ==4):
            result = 1
            break
        if matrix['O'] == 4 or (matrix['O'] + matrix['T'] ==4):
            result = -1
            break

    if result == 1:
        return 'X won'
    if result == -1:
        return 'O won'
    if full == 1:
        return 'Draw'
    else:
        return 'Game has not completed'


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        ten = []

        for i in xrange(10):
            ten.append({'X':0,'O':0, 'T':0, '.':0 })
        for i in xrange(4):
            row = f.readline()
            for j in xrange(4):
                ten[i][row[j]] +=1
                ten[4+j][row[j]] +=1
                if i == j:
                    ten[8][row[j]] +=1
                    continue
                if i+j ==3:
                    ten[9][row[j]] +=1
                    continue
        f.readline()
        print "Case #%d: %s" % (_t+1, tic(ten))

