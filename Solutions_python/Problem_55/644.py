
for T in xrange(input()):
    R, k, N = [int(x) for x in raw_input().split() ]
    next_groups = [ int(x) for x in raw_input().split() ]
    #print "%d %d %d %s" % (R, k, N, str(next_groups))
    money = 0
    for ri in xrange(R):
        people = 0
        groups = list(next_groups)
        end_i = len(groups)
        for i in xrange(end_i):
            gi = groups[i]
            if people + gi > k:
                end_i = i
                #next_groups.extend( groups[i:] )
                #print "i> %s" % (str(next_groups))
                break
            else:
                people += gi
                # move to last
                #next_groups.append(gi);
                #print "i> %s" % (str(next_groups))
        #print "%d %s" % (end_i, str(groups[:end_i]))
        #print "%s" % ( str(groups[end_i:]))
        next_groups = groups[end_i:]
        next_groups.extend(groups[:end_i])
        #print "%d %s" % (end_i, str(next_groups))
        money += people
    print "Case #%d: %d" % (T+1, money)
