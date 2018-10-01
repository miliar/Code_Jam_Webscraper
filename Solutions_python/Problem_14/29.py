import sys


def process(r1):
    line = r1.readline()
    f = line.split(" ")
    n = int(f[0])
    m = int(f[1])
    a = int(f[2])
    for x1 in xrange(n+1):
        for y1 in xrange(m+1):
            for x2 in xrange(n+1):
                for y2 in xrange(m+1):
                    if calc_s(x1, y1, x2, y2) == a:
                        return [x1, y1, x2, y2]
    else:
        return []

def calc_s(x1, y1, x2, y2):
    s=  (x1*y2 - x2*y1)
    if s >= 0:
        return s
    else:
        return -s
def main():
    if len(sys.argv) == 2:
        #print sys.argv
        r1 = open(sys.argv[1])
    else:
        print "input filename"
        sys.exit()
    case_str = r1.readline()
    case = int(case_str)
    w1 = open("output.txt", "w")
    for i in xrange(case):
        result = process(r1)
        if len(result) == 0:
            print "Case #%d: IMPOSSIBLE"%(i+1)
            w1.write("Case #%d: IMPOSSIBLE\n"%(i+1))
        else:
            print "Case #%d: 0 0 %d %d %d %d"%(i+1, result[0], result[1], result[2], result[3])
            w1.write("Case #%d: 0 0 %d %d %d %d\n"%(i+1, result[0], result[1], result[2], result[3]))
main()
