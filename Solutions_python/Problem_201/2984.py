
f_in = open('C-small-1-attempt0.in', 'r')
# T = 1
T = int(f_in.readline())

for rounds in range(T):
    line = f_in.readline()
    line = line.split(' ')
    N = int(line[0])
    K = int(line[1])

    l_s = [int]*N
    r_s = [int]*N
    used = [bool]*N
    selected_stall = int

    for i in range(N):
        l_s[i] = i
        r_s[i] = N - 1 - i
        used[i] = False
    for i in range(K):
        min_list = []
        for k in range(N):
            min_list.append(min(l_s[k], r_s[k]))

        max_of_min = max(min_list)
        option_list_min = [o for o, j in enumerate(min_list) if j == max_of_min]
        short_max_list = []
        for k in option_list_min:
            short_max_list.append(max(l_s[k], r_s[k]))

        max_of_max = max(short_max_list)
        selected_stall = option_list_min[short_max_list.index(max_of_max)]

        used[selected_stall] = True
        answer_l = l_s[selected_stall]
        l_s[selected_stall] = 0
        answer_r = r_s[selected_stall]
        r_s[selected_stall] = 0

        k = 1
        while selected_stall - k >= 0 and not used[selected_stall - k]:
            r_s[selected_stall - k] = k-1
            k += 1
        k = 1
        while selected_stall + k < N and not used[selected_stall + k]:
            l_s[selected_stall + k] = k-1
            k += 1

        min_list.clear()
        short_max_list.clear()

    print(f'case #{str(rounds+1)}: {str(max(answer_l, answer_r))} {str(min(answer_l, answer_r))}')

f_in.close()
