f = open("c:/users/roy/Downloads/A-small-attempt0.in")
#f = open("C:/Users/Roy/Documents/gcj/test.in.txt")

nCnt = 0
lines = f.readlines()

#print len(lines)

nCnt = int(lines[0])
#print "There are %i test cases." % nCnt
nCase = 0

nLineNo = 1
for nCase in range(1, nCnt+1):
    #print "Case #%i:" % nCase
    vals = lines[nLineNo].split()
    nLineNo = nLineNo + 1
    n = int(vals[0])
    A = int(vals[1])
    B = int(vals[2])
    C = int(vals[3])
    D = int(vals[4])
    x0 = int(vals[5])
    y0 = int(vals[6])
    M = int(vals[7])
    trees = []
    X = x0
    Y = y0
    trees.append((X, Y))
    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append((X, Y))
    #print str(trees)
    # i = tree #1, j = tree #2, k = tree #3
    count = 0
    l = len(trees)
    for i in range(0, l):
        tree1 = trees[i]
        for j in range(i+1, l):
            tree2 = trees[j]
            for k in range(j+1, l):
                tree3 = trees[k]
                #print "%s, %s, %s" % (str(tree1), str(tree2), str(tree3))
                xc = (tree1[0] + tree2[0] + tree3[0])
                if xc % 3 == 0:
                    xc = xc / 3
                else:
                    continue
                yc = (tree1[1] + tree2[1] + tree3[1])
                if yc % 3 == 0:
                    yc = yc / 3
                else:
                    continue
                #print "(xc, yc) = %s, %s" % (xc, yc)
                #print "Ok!"
                count = count + 1
    print "Case #%i: %i" % (nCase, count)