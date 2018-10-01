def get_left_empty_stalls(x):
    Ls = 0
    y = 1
    while x-y > 0:
        if (stalls[x-y] == '.'):
            Ls += 1
        else:
            break
        y += 1
    return Ls

def get_right_empty_stalls(x):
    Rs = 0
    y = 1
    while x+y < len(stalls)-1:
        if (stalls[x+y] == '.'):
            Rs += 1
        else:
            break
        y += 1
    return Rs


t = int(raw_input())

for i in range(t):
    n, k = [int(s) for s in raw_input().split()]

    stalls = ['.'] * n
    stalls.insert(0, 'O')
    stalls.append('O')

    last_chosen_stall = None

    for j in range(k):
        empty_stalls = {}
        min_ls_rs_dict = {}
        max_min_ls_rs = 0

        for x, val in enumerate(stalls[0:len(stalls)]):
            if val == '.':
                empty_stalls[x] = {}

                ls = get_left_empty_stalls(x)
                rs = get_right_empty_stalls(x)
                min_ls_rs = min(ls, rs)
                max_ls_rs = max(ls, rs)

                empty_stalls[x]['max_ls_rs'] = max_ls_rs

                if min_ls_rs not in min_ls_rs_dict:
                    min_ls_rs_dict[min_ls_rs] = []
                min_ls_rs_dict[min_ls_rs].append(x)

                max_min_ls_rs = max(min_ls_rs, max_min_ls_rs)

        if len(empty_stalls) < 1:
            break
        else:   
            farthest_closest_neighbors = min_ls_rs_dict[max_min_ls_rs]

            max_max_ls_rs = -1
            chosen_stall = None

            for x in farthest_closest_neighbors:
                if empty_stalls[x]['max_ls_rs'] > max_max_ls_rs:
                    max_max_ls_rs = empty_stalls[x]['max_ls_rs']
                    chosen_stall = x

            stalls[chosen_stall] = 'O'
            last_chosen_stall = chosen_stall

    ls = get_left_empty_stalls(last_chosen_stall) if last_chosen_stall is not None else 0
    rs = get_right_empty_stalls(last_chosen_stall) if last_chosen_stall is not None else 0
    min_ls_rs = min(ls, rs)
    max_ls_rs = max(ls, rs)
    print "Case #{}: {} {}".format(i+1, max_ls_rs, min_ls_rs)
