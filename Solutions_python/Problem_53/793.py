import sys
import psyco
psyco.full()

def snappers(n, k):
    return (k - (2**n-1)) % 2**n == 0

def off(b):
    if b:
        return "ON"
    return "OFF"

def main():
    f = sys.stdin
    casos = int(f.readline())
    i = 1
    for c in range(casos):
        l = f.readline()
        cosas = l.split()
        n, k = [int(x) for x in cosas]
        print "Case #%s: %s" % (i, off(bool(snappers(n,k))))
        i = i+1

if __name__ == '__main__':
    main()

