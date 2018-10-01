T = int(raw_input())  

for K in xrange (T):
    n, p= [int(g) for g in raw_input().split(" ")]
    #print n, p
    receipt = [int(g) for g in raw_input().split(" ")]
    #print receipt
    q = []
    for i in xrange(n):
        line = [int(g) for g in raw_input().split(" ")]
        line.sort()
        q.append(line)
    #print q

    ans = 0
    mark = 0
    while q[0]:
        kit = int(q[0][0] / (receipt[0] * 1.1)) + mark
        #print kit, q
        if (receipt[0] * 0.9 * kit > q[0][0]):
            q[0].pop(0)
            mark = 0
        elif (receipt[0] * 1.1 * kit < q[0][0]):
                mark += 1
        elif (kit * receipt[0] * 0.9 <= q[0][0] <= kit * receipt[0] * 1.1):
            bb = True
            for i in xrange(1, n):
                while (q[i] and receipt[i] * 0.9 * kit > q[i][0]):
                    q[i].pop(0)
                if not q[i]:
                    bb = False;
                    break;
                if not (kit * receipt[i] * 0.9 <= q[i][0] <= kit * receipt[i] * 1.1):
                    bb = False
                    break;

            if bb:
                for i in xrange(n):
                    if q[i]:
                        q[i].pop(0)
                    else:
                        break;
                ans += 1
                mark = 0
            else:
                mark += 1
            #print bb
        else:
            q[0].pop(0)
        #print kit, ans, q

    print "Case #{}: {}".format(K+1, ans)
