f = open ("A-large.in")
out = open ("A-large.out", "w")

N = int(f.readline())

for c in xrange (N):
    dic = {}
    switches = 0
    S = int(f.readline())
    for i in xrange(S):
        f.readline()

    Q = int(f.readline())
    for i in xrange(Q):
        w = f.readline().strip()
        dic[w] = "1"
        if len(dic) == S:
            # print dic
            switches += 1
            dic = {}
            dic[w] = "1"
    out.write("Case #" + str(c+1) + ": " + str(switches) + "\n")
out.flush()
out.close()
