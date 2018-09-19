IN = 'A-small-attempt4.in'
#IN = 'bull.in'
OUT = 'bull.out'

def print_res(f, c, r):
    f.write("Case #%d: %d\n" % (c, r))


def find_r(r, N):
    s = 0
    c = 0
    for i in xrange(0,2000+2, 2):
        s += 2*r + 2*i + 1
        if s > N:
            return c
        c+=1

def main():
    fi = open(IN)
    fo = open(OUT, 'w')
    size = int(fi.readline())
    #print size
    for i in xrange(1, size+1):
        r,t = map(int, fi.readline().strip().split())
        res = find_r(r, t)
        print_res(fo, i, res)
    fi.close()
    fo.close()
main()
