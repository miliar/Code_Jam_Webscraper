c = int(raw_input())
for cc in xrange(c):
    max_n, cnt = raw_input().strip().split()
    
    add = 0
    standing = 0
    for required, people in enumerate(map(int, cnt)):
        add += max(0, required - (standing + add))
        standing += people

    print 'Case #%d: %d' % (1+cc, add)

