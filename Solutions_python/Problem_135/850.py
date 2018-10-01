def read():
    return map(int, raw_input().split())

fp = open('ans.txt', 'w')
for CaseNum in xrange(input()):
    lnum_a = input() - 1
    a = [read() for i in xrange(4)]
    lnum_b = input() - 1
    b = [read() for i in xrange(4)]
    ans = []
    for idx in xrange(4):
        for idy in xrange(4):
            if a[lnum_a][idx] == b[lnum_b][idy]:
                ans.append(a[lnum_a][idx])
    
    if len(ans) == 1:
        fp.write('Case #%d: %d\n' % (CaseNum + 1, ans[0]))
    elif len(ans) > 1:
        fp.write('Case #%d: Bad magician!\n' % (CaseNum + 1, ))
    else:
        fp.write('Case #%d: Volunteer cheated!\n' % (CaseNum + 1, ))
    
