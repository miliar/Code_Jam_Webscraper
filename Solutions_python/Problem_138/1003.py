def deceitful(n, k):
    point = 0
    for i in range(len(n)):
        if n[len(n) - i - 1] > k[-1]:
            n.remove(n[len(n) - i - 1])
            k.remove(ken[-1])
            point = 1
            break
    return point, n, k


cts = input()
for ct in range(1, cts + 1):
    nblocks = input()
    naomi = [float(entry) for entry in raw_input().split()]
    ken = [float(entry) for entry in raw_input().split()]

    naomi.sort(reverse=True)
    ken.sort(reverse=True)
    
    war = 0
    naomi2 = list(naomi)
    ken2 = list(ken)
    while len(naomi2):
        if naomi2[0] > ken2[0]:
            ken2.remove(ken2[-1])
            war += 1
        else:
            for i in range(len(ken2)):
                if naomi2[0] > ken2[i]:
                    if i == 0:
                        ken2.remove(ken2[0])
                    else:
                        ken2.remove(ken2[i - 1])
                    break
        naomi2.remove(naomi2[0])

    #cheating = 0
    #points = 0
    #while len(naomi):
    #    print naomi
    #    print ken
    #    print "war: %.3f, %.3f" % (naomi[0], ken[0])
    #    if naomi[0] > ken[0]:
    #        for i in range(len(naomi)):
    #            if naomi[i] < ken[0]:
    #                if i != 0:
    #                    print "out1: %.3f, %.3f" % (naomi[i - 1], ken[-1])
    #                    naomi.remove(naomi[i - 1])
    #                else:
    #                    print "out1: %.3f, %.3f" % (naomi[0], ken[-1])
    #                    naomi.remove(naomi[0])
    #                break
    #            if i == len(naomi) - 1:
    #                print "out1: %.3f, %.3f" % (naomi[0], ken[-1])
    #                naomi.remove(naomi[0])
    #        cheating += 1
    #        ken.remove(ken[-1])
    #    else:
    #        print "out2: %.3f, %.3f" % (naomi[-1], ken[0])
    #        naomi.remove(naomi[-1])
    #        ken.remove(ken[0])
    #        points+=1
    #    print "naomi: %d -- ken: %d " % (cheating, points)
    #    print

    #print naomi
    #print ken
    #print nblocks

    cheating = 0
    point = 1
    while point:
        point, naomi, ken = deceitful(naomi, ken)
        cheating += point

    print "Case #%d: %d %d" % (ct, cheating, war)
