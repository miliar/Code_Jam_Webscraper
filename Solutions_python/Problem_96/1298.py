import sys

valid = lambda (a, b, c): max(a, b, c) - min(a, b, c) <= 2

surp = lambda (a, b, c): max(a, b, c) - min(a, b, c) == 2

best = lambda (a, b, c): max(a, b, c)

f = open(sys.argv[1])
t = int(f.readline())
for _t in xrange(t):
    line = f.readline()
    N, S, p = map(int, line.split()[0:3])
    ti = map(int, line.split()[3:])
    arr = []
    for score in ti:
        scores = []
        for c in xrange(0, 11):
            for b in xrange(0, c + 1):
                for a in xrange(0, b + 1):
                    if valid((a, b, c)) and a + b + c == score:
                        scores.append((a, b, c))
        arr.append(scores)
    if N == 1:
        c = 0 
        for score in arr[0]:
            if surp(score) and S == 1:
                if best(score) >= p: c = 1
            elif not surp(score) and S == 0:
                if best(score) >= p: c = 1
    elif N == 2:
        c = 0
        for score1 in arr[0]:
            for score2 in arr[1]:
                if S == 2 and surp(score1) and surp(score2):
                    if best(score1) >= p and best(score2) >= p: c = 2
                    elif best(score1) >= p or best(score2) >= p: c = max(c, 1)
                elif S == 1 and ((surp(score1) and not surp(score2)) or (not surp(score1) and surp(score2))):
                    if best(score1) >= p and best(score2) >= p: c = 2
                    elif best(score1) >= p or best(score2) >= p: c = max(c, 1)
                elif S == 0 and not surp(score1) and not surp(score2):
                    if best(score1) >= p and best(score2) >= p: c = 2
                    elif best(score1) >= p or best(score2) >= p: c = max(c, 1)
    else:
        c = 0
        for s1 in arr[0]:
            for s2 in arr[1]:
                for s3 in arr[2]:
                    if S == 3 and surp(s1) and surp(s2) and surp(s3):
                        if best(s1) >= p and best(s2) >= p and best(s3) >= p: c = 3
                        elif (best(s1) >= p and best(s2) >= p) or (best(s2) >= p and best(s3) >= p) or (best(s3) >= p and best(s1) >= p): c = max(c, 2)
                        elif best(s1) >= p or best(s2) >= p or best(s3) >= p: c = max(c, 1)
                    elif S == 2 and ((surp(s1) and surp(s2) and not surp(s3)) or (surp(s2) and surp(s3) and not surp(s1)) or (surp(s3) and surp(s1) and not surp(s2))):
                        if best(s1) >= p and best(s2) >= p and best(s3) >= p: c = 3
                        elif (best(s1) >= p and best(s2) >= p) or (best(s2) >= p and best(s3) >= p) or (best(s3) >= p and best(s1) >= p): c = max(c, 2)
                        elif best(s1) >= p or best(s2) >= p or best(s3) >= p: c = max(c, 1)
                    elif S == 1 and ((surp(s1) and not surp(s2) and not surp(s3)) or (surp(s2) and not surp(s3) and not surp(s1)) or (surp(s3) and not surp(s1) and not surp(s2))):
                        if best(s1) >= p and best(s2) >= p and best(s3) >= p: c = 3
                        elif (best(s1) >= p and best(s2) >= p) or (best(s2) >= p and best(s3) >= p) or (best(s3) >= p and best(s1) >= p): c = max(c, 2)
                        elif best(s1) >= p or best(s2) >= p or best(s3) >= p: c = max(c, 1)
                    elif S == 0 and not surp(s1) and not surp(s2) and not surp(s3):
                        if best(s1) >= p and best(s2) >= p and best(s3) >= p: c = 3
                        elif (best(s1) >= p and best(s2) >= p) or (best(s2) >= p and best(s3) >= p) or (best(s3) >= p and best(s1) >= p): c = max(c, 2)
                        elif best(s1) >= p or best(s2) >= p or best(s3) >= p: c = max(c, 1)
    print 'Case #%d: %d' % (_t + 1, c)
