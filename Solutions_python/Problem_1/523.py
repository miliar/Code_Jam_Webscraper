S = dict()
Q = list()
inS = {}

n = 0
q = 0


from sys import argv
inpath = "A.in"
if len(argv) > 1:
    inpath = str(argv[1])

if __name__ == "__main__":
    f = open(inpath, "r")
    n_kase = int(f.readline())
    for kase in range(n_kase):
        S.clear()
        Q = []
        n = int(f.readline())
        #print n

        for i in range(n):
            c = f.readline()[:-1]
            S[c] = c
            #print S[c]

        #print S

        q = int(f.readline())
        #print q

        k = 0
        for i in range(q):
            c = f.readline()[:-1]
            #print ">",c
            if S.has_key(c):
                if k == 0 or Q[k-1] != c:
                    Q.append(c)
                    k += 1
        
        #print Q, k
        num_q = len(Q)
        print "Case #%d:" % ( kase+1) ,

        if num_q < n:
            print 0
        elif num_q == n:
            print 1
        else:
            new_set = set()
            count = 0
            for item in Q:
                new_set.add(item)
                if len(new_set) == n:
                    count += 1
                    new_set.clear()
                    new_set.add(item)
            print count