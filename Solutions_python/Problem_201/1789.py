t = int(raw_input().strip())
for i in range(t):
    n, k = map(int, raw_input().strip().split())
    empty_stalls_list = [n]

    for j in range(k):
        max_empty_stalls = max(empty_stalls_list)
        insert_index = empty_stalls_list.index(max_empty_stalls)
        if max_empty_stalls % 2 == 0:
            new_empty_stalls_left = max_empty_stalls / 2 - 1
        else:
            new_empty_stalls_left = max_empty_stalls / 2

        new_empty_stalls_right = max_empty_stalls - 1 - new_empty_stalls_left
        empty_stalls_list[insert_index] = new_empty_stalls_left
        empty_stalls_list.insert(insert_index + 1, new_empty_stalls_right)

        if j == k-1:
            print "Case #{0}: {1} {2}".format(
                i + 1, max(new_empty_stalls_right, new_empty_stalls_left), min(
                    new_empty_stalls_right, new_empty_stalls_left))
