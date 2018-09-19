f = open('C-small-attempt0.in', 'r')
lines = f.readlines()
f.close()

case_count = int(lines.pop(0))

for case in xrange(1, case_count+1):
    R, k, N = (int(i) for i in lines.pop(0).strip().split(' '))
    q = [int(i) for i in lines.pop(0).strip().split(' ')]
    sum = 0
    for i in xrange(0, R):
        rq = []
        pad = 0
        dequeue = True
        while dequeue and len(q) > 0:
            front = q[0]
            if pad + front <= k:
                pad += q.pop(0)
                rq.append(front)
            else:
                dequeue = False
        sum += pad
        q += rq
    print 'Case #%d: %d' % (case, sum)

