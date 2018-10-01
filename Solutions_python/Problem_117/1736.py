T = input()
output = []
for i in xrange(T):
    (N, M) = raw_input().split()
    N = int(N); M = int(M)
    a = [[]]*N
    for n in xrange(N):
        num_str = raw_input()
        a[n] = num_str.split()
    skip = False
    for n in xrange(N):
        if skip:
            break
        for m in xrange(M):
            if skip:
                break
            s1 = True; s2 = True
            for column in xrange(M):
                if a[n][column] > a[n][m]:
                    s1 = False;
                    break;
            for row in xrange(N):
                if a[row][m] > a[n][m]:
                    s2 = False;
                    break;
            if (s1 == False) and (s2 == False):
                skip = True
                output.append('NO')
                break;
    if skip == False:
        output.append('YES')
for i in xrange(len(output)):
    print "Case #%d: %s" %(i+1, output[i])

