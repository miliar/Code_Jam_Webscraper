import sys

def checkcase(n,k):
#    print n,k,(k+1) % (2**n)
    if (k+1) % (2**n) == 0:
        return True
    else:
        return False

def readinput(fname):
    for i,line in enumerate(open(fname)):
        if i == 0:
            T = int(line.strip())
        else:
            [n,k] = [int(x) for x in line.strip().split()]
            if checkcase(n,k):
                flg = "ON"
            else:
                flg = "OFF"
            print "Case #%d: %s"%(i,flg)


def main():
    readinput(sys.argv[1])

if __name__ == '__main__':
    main()





