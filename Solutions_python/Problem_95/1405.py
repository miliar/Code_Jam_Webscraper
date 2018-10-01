import sys, math
from multiprocessing import Pool

def init():
    msgs = (("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"),
           ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
           ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"),
           ("y qeez", "a zooq"),
           )
    d = dict()
    for msg in msgs:
        for i,j in zip(*msg):
            if i not in d:
                d[i] = j
            elif d[i] != j:
                print "ERROR! i=%s, j=%s, d[i]=%s" % (i, j, d[i])
                break
#    letters = "qwertuiopasdfgjklzxcvbnm"
#    for c in letters:
#        if c not in d:
#            print c
#        if c not in d.values():
#            print c
    return d
                
if __name__ == "__main__":
    d = init()
#    print len(d)
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = open("test.txt")
    T = int(f.readline())
    for i in range(T):
        case = f.readline().strip()
        result = [d[c] for c in case]
        print "Case #%d: %s" % (i+1, "".join(result))
            