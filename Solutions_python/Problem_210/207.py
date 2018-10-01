t = int(input())  # read a line with a single integer
for ii in range(1, t + 1):
    a_c, a_j = [int(s) for s in input().split(" ")]

    time_c = []
    for c in range(a_c):
        start, end = [int(s) for s in input().split(" ")]
        time_c.append((start, end, "a"))

    time_j = []
    for j in range(a_j):
        start, end = [int(s) for s in input().split(" ")]
        time_j.append((start, end, "b"))

    time = time_c + time_j

    time.sort()

    # extend the list

    added_time = []

    for i in range(len(time) - 1):
        t = time[i]
        t_next = time[i + 1]

        t_s, t_e, t_t = t
        n_s, n_e, n_t = t_next

        if t_e == n_s:
            continue
        if t_t != n_t:
            new_type = "ab"
        elif t_t == "a":
            new_type = "aa"
        else:
            new_type = "bb"

        new_time = (t_e, n_s, new_type)
        added_time.append(new_time)

    first = time[0]
    last = time[-1]

    t_s, t_e, t_t = last
    n_s, n_e, n_t = first

    if t_e == n_s:
        continue
    if t_t != n_t:
        new_type = "ab"
    elif t_t == "a":
        new_type = "aa"
    else:
        new_type = "bb"

    if t_e == 1440:
        if n_s == 0:
            new_time = None
        else:
            new_time = (0, n_s, new_type)

    elif n_s == 0:
        new_time = (t_e, 1440, new_type)
    else:
        new_time = (t_e, 1440 + n_s, new_type)

    if new_time is not None:
        added_time.append(new_time)

    time += added_time

    time.sort()
    # print (time)

    while True:
        sum_a = 0
        sum_b = 0
        sum_ab = 0

        max_aa = None
        max_aa_l = 0

        max_bb = None
        max_bb_l = 0
        for i in range(len(time)):
            t = time[i]
            t_s, t_e, t_t = t
            if t_t == "a" or t_t == "aa":
                if t_t == "aa" and t_e - t_s > max_aa_l:
                    max_aa = i
                    max_aa_l = t_e - t_s

                sum_a += t_e - t_s

            elif t_t == "b" or t_t == "bb":
                if t_t == "bb" and t_e - t_s > max_bb_l:
                    max_bb = i
                    max_bb_l = t_e - t_s

                sum_b += t_e - t_s
            else:
                sum_ab += t_e - t_s

        # print ("a, b, ab,", sum_a, sum_b, sum_ab)
        if sum_b + sum_ab >= 720 and sum_a + sum_ab >= 720:
            break
        elif sum_b + sum_ab < 720:
            # print(sum_b, sum_ab)
            # aa -> b
            t_s, t_e, t_t = time[max_aa]
            time[max_aa] = (t_s, t_e, "b")
            if t_e - t_s + sum_b + sum_ab >= 720:
                break
        else:
            t_s, t_e, t_t = time[max_bb]
            time[max_bb] = (t_s, t_e, "a")
            if t_e - t_s + sum_a + sum_ab >= 720:
                break

    count = 0

    for i in range(len(time)):
        t_s, t_e, t_t = time[i]
        time[i] = (t_s, t_e, t_t[0])

    # print (time)
    for i in range(len(time) - 1):  # find number of transitions
        t = time[i]
        t_next = time[i + 1]

        t_s, t_e, t_t = t
        n_s, n_e, n_t = t_next

        if (t_t != n_t):
            count += 1

    first = time[0]
    last = time[-1]

    t_s, t_e, t_t = last
    n_s, n_e, n_t = first
    if t_t != n_t:
        count += 1

    print("Case #{}: {}".format(ii, count))
