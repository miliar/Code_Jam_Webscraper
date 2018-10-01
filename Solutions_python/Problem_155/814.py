for t in range(int(input())):
    smax, crowd = input().split()
    crowd = [int(x) for x in crowd]

    friends_added = 0
    people_standing_up = 0

    for level, people in enumerate(crowd):
        if people == 0:
            continue

        if level > people_standing_up:
            to_add = level - people_standing_up
            friends_added += to_add
            people_standing_up += to_add

        people_standing_up += people

    print('Case #{0}: {1}'.format(t+1, friends_added))
