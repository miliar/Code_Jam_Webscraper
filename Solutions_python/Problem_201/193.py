from sortedcontainers import SortedDict
for case in range(1,1+int(raw_input())):
    N, K = map(int, raw_input().split(' '))
    blocks = SortedDict({N: 1})
    while K:
        b, n = blocks.popitem()
        if n >= K:
            print "Case #%d: %d %d" % (case, b/2, (b-1)/2)
            break
        blocks.setdefault(b/2, 0)
        blocks[b/2] += n
        blocks.setdefault((b-1)/2, 0)
        blocks[(b-1)/2] += n
        K -= n
