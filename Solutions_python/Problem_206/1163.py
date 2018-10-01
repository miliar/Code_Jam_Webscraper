t = int(raw_input())

curr_case = 1;
while curr_case <= t:
    d, n = [int(s) for s in raw_input().split(" ")]

    # print "Annies:", d, n

    slowest_horse = 0
    for horse in range(n):
        k, s = [int(i) for i in raw_input().split(" ")]

        horse_travel_time = float(d - k) / float(s)
        if (slowest_horse < horse_travel_time):
            slowest_horse = horse_travel_time

    annie_travel_time = float(d) / float(slowest_horse)
    print "Case #{0}: {1}".format(curr_case, annie_travel_time)

    curr_case += 1