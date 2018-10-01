from math import pi
T = int(raw_input())

for case in range(1, T + 1):
    all_c = []
    N, K = map(int, raw_input().strip().split())
    for i in range(N):
        C = map(int, raw_input().strip().split())
        all_c.append(C)
    c_sorted = sorted(all_c, key=lambda x: x[0] * x[1], reverse=True)

    max_size = 0
    current_size = 0
    for base_index, base in enumerate(c_sorted):
        br, bh = base
        counter = 1
        current_size = pi * (br*br + 2 * br * bh)
        for item_index, item in enumerate(c_sorted):
            if item_index == base_index:
                continue
            if counter == K:
                break

            ir, ih = item
            if ir <= br:
                current_size += pi * 2 * ir * ih
                counter += 1

        if counter == K and current_size > max_size:
            max_size = current_size

    print "Case #{}: %0.9f".format(case) % max_size




