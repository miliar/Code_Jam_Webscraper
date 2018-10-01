import sys

T = int(raw_input())

for t in range(1, T+1):
    N,P = map(int, raw_input().split())

    Rs = map(int, raw_input().split())
    Qs = []
    for i in range(N):
        Qs.append(sorted(map(int, raw_input().split())))

    num = 0
    for pi in range(P):
        if len(Qs[0]) == 0: break
        s = int(round(Qs[0][0] / float(Rs[0])))
        s_range = (int(Qs[0][0] / 1.1 / Rs[0]), int(Qs[0][0] / 0.9 / Rs[0]))
        num_kits, Qs_inlimit = 0, None
        for s in range(s_range[0], s_range[1]+1):
            Rs_limit = [ (0.9*x*s, 1.1*x*s) for x in Rs ]
            Qs_inlimit_tmp = [ filter(lambda q:limit[0] <= q and q <= limit[1], packs) for packs, limit in zip(Qs, Rs_limit) ]
            num_kits_tmp = min(map(len, Qs_inlimit_tmp))
            if num_kits_tmp > num_kits:
                num_kits = num_kits_tmp
                Qs_inlimit = Qs_inlimit_tmp

        #print s, Rs_limit
        #print Qs_inlimit
        #print num_kits
        if num_kits == 0:
            Qs[0].pop(0)
            #print Qs
            continue
        num += num_kits

        for ingi in range(N):
            for j in range(num_kits):
                Qs[ingi].remove(Qs_inlimit[ingi][j])

        #print Qs



    print 'Case #%d: %d' % (t, num)
