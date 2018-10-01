def main(index):
    print 'Case #%d:' % index,
    N, K = map(int, raw_input().split())
    queue = {}
    Ns = []
    Ns.append(N)
    queue[N] = 1
    index = 0
    while K:
        N = Ns[index]
        N1 = N / 2
        N2 = (N-1) / 2
#        print index, N, N1, N2, K, queue[N]
        if K <= queue[N]:
            print N1, N2
            return
        if N1 in Ns:
            queue[N1] += queue[N]
        else:
            queue[N1] = queue[N]
            Ns.append(N1)
        if N2 in Ns:
            queue[N2] += queue[N]
        else:
            queue[N2] = queue[N]
            Ns.append(N2)
        K -= queue[N]
        index += 1



T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
