import math

def output(t, res):
    casestr = "Case #" + str(t+1) + ": "
    status = str(res) if res is not None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine


def main():
    T = int(raw_input())

    for t in xrange(T):
        N, K = map(int, raw_input().split(' '))

        d1 = N+1
        k_log = int(math.log(K, 2))
        k2 = 1 << k_log
        r = K - k2

        d = d1 >> k_log
        e = d1 - (d << k_log)

        if r < e:
            res = d+1
        else:
            res = d

        #print "K=", K, "k_log=", k_log, "k2=", k2, "d1=", d1, "d=", d, "e=", e, "r=", r

        res = (res - 2)
        m = res >> 1
        n = res - m
        output(t, str(n) + ' ' + str(m))
        # stalls = [False]*(N+2)
        # stalls[0] = True
        # stalls[N+1] = True
        #
        # for i in xrange(K):
        #     min_dist, max_dist, pos = getDist(stalls)
        #     print "k="+ str(i+1), "d=" + str(min_dist+max_dist+2)
        #     if stalls[pos]:
        #         print "NOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!", min_dist, max_dist, pos, stalls
        #         exit()
        #     stalls[pos] = True
        #
        # output(t, str(max_dist) + " " + str(min_dist))


def getDist(stalls):
    d = 0

    max_min_dist = -1
    max_max_dist = -1
    min_pos = 0
    for i in xrange(1, len(stalls)):
        d += 1
        if stalls[i]:
            L = d/2
            R = d - L
            pos_curr = i - R
            #print "d==", d

            R -= 1
            L -= 1

            min_curr = min(L, R)
            max_curr = max(L, R)

            if min_curr > max_min_dist \
                    or min_curr == max_min_dist and max_curr > max_max_dist \
                    or min_curr == max_min_dist and max_curr == max_max_dist and pos_curr < min_pos:
                max_min_dist = min_curr
                max_max_dist = max_curr
                min_pos = pos_curr
                #print "d==", d

            d = 0


    return max_min_dist, max_max_dist, min_pos

if __name__ == "__main__":
    main()