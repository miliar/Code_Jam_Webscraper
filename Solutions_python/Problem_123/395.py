T = int(input())

for casen in xrange(T):
    A, N = map(int, raw_input().split())
    mote_set = map(int, raw_input().split())
    mote_set = sorted(mote_set)
    total = 0

    while mote_set != []:
        
        if mote_set[0] < A:
                A += mote_set[0]
                mote_set = mote_set[1:]

        else:
            nb_mote= len(mote_set)

            cache = mote_set
            cache_A = A
            i = 0
            while cache != [] and i <= nb_mote:
                if cache_A > cache[0]:
                    cache_A += cache[0]
                    cache = cache[1:]
                else:
                    cache_A += cache_A-1
                    i += 1

            if cache == []:
                while A <= mote_set[0]:
                    A += A-1
                    total += 1
                A += mote_set[0]
                mote_set = mote_set[1:]
            else:
                total += len(mote_set)
                mote_set = []

    print "Case #{}: {}".format(casen+1, total)
