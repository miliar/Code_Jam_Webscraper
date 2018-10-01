for t in xrange(1, input()+1):
    n, k = map(int, raw_input().split())
    print "Case #" + str(t) + ":",
    if n == k:
        z = y = 0
        print y, z
    else:
        # print "#stalls, #people",n, k
        target = k
        level = counter = 0
        result = val = {}
        result[level] = [n]
        while k > 0:
            k -= 2 ** level
            level += 1
            result[level] = []
            for i in result[level - 1]:
                i = i - 1
                L = i / 2
                R = i - L
                result[level].append(R)
                result[level].append(L)
                # print "index: ", counter
                # print result[level]
                counter += 1
                if counter == target:
                    # print "target: ", target
                    # print "counter: ", counter
                    # # index = len(result[level])-counter
                    # # print "index: ", index
                    z = result[level][-1]
                    y = result[level][-2]
                    break
                else:
                    if R == 0 and L == 0:
                        z = y = 0
                        break
            result[level].sort(reverse=True)
            # print counter, result[level]
        print y, z
