import sys


def clicker_time(C, F, X):
    fxs = 0
    value = X / 2
    stop = False
    ii = 0
    while not stop:
        fxs += ((C / (2 + ii * F)))
        ii += 1
        new_value = fxs + (X / (2 + ii * F))
        if new_value < value:
            value = new_value
        else:
            stop = True
    return value


def main(argv):
    file_ = open(argv[1], 'r')
    file_.next()
    case = 1
    for line in file_:
        C, F, X = map(float, line.strip("\n").split(" "))
        result = clicker_time(C, F, X)
        print "Case #{case}: {result:0.7f}".format(case=case, result=result)
        case += 1

if __name__ == '__main__':
    main(sys.argv)
