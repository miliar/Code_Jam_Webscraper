def standing_ovation():
    T = int(raw_input())
    for case in xrange(T):
        audience = [int(x) for x in raw_input().strip().split()[1]]
        clapping = 0
        friends_invited = 0
        for lvl, ppl in enumerate(audience):
            if clapping < lvl:
                new_friends = (lvl - clapping)
                friends_invited += new_friends
                clapping += new_friends
            clapping += ppl
        print "Case #%d: %d" % (case+1, friends_invited)


standing_ovation()

