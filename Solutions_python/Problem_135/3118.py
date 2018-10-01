def solve(x):
    A, B = [], []
    Arow = int(raw_input())
    for i in xrange(4):
        row = raw_input().split(' ')
        A.append(row)
    Brow = int(raw_input())
    for i in xrange(4):
        row = raw_input().split(' ')
        B.append(row)
    t = [k for k in A[Arow-1] if k in B[Brow-1]]
    ans = "Volunteer cheated!"
    if len(t) == 1:
        ans = t[0]
    elif len(t) > 1:
        ans = "Bad magician!"
    print "Case #%d: %s" % (x, ans)

T = int(raw_input())
for i in xrange(T):
    solve(i+1)
