if __name__ == '__main__':
    for case in xrange(int(raw_input())):
        N, K, B, T = [int(s) for s in raw_input().split()]
        xs = [int(s) for s in raw_input().split()]
        vs = [int(s) for s in raw_input().split()]

        # handle the case the two chicks start at the same location
        xvs = [(xs[i], vs[i]) for i in xrange(N)]
        xvs.sort(key=lambda x: (x[0], -x[1]))
        xs = [p[0] for p in xvs]
        vs = [p[1] for p in xvs]

        slow = 0
        fast = 0
        swaps = 0
        i = N - 1
        while i >= 0 and fast < K:
            if (B - xs[i]) <= T * vs[i]:
                fast += 1
                swaps += slow
            else:
                slow += 1

            i -= 1

        if fast < K:
            res = 'IMPOSSIBLE'
        else:
            res = str(swaps)

        print 'Case #%d: %s' % (case+1, res)
