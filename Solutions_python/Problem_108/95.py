for t in range(int(raw_input())):
    vines = []
    for n in range(int(raw_input())):
        vines.append(map(int, raw_input().split(' ')))
    D = int(raw_input())

    # base state is being at a distance holding a vine
    reaches = [vines[0][0]*2]
    for i, vine in enumerate(vines[1:]):
        best_reach = 0
        for j, r in enumerate(reaches):
            if r >= vine[0]:
                new_reach = vine[0] + min(vine[0] - vines[j][0], vine[1])
                best_reach = max(best_reach, new_reach)
        reaches.append(best_reach)

    print "Case #%d: %s" % (t+1, max(reaches) >= D and "YES" or "NO")
