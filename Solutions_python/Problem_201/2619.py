def smart_solution(n, k):
    occupied_stalls = [0, n + 1]

    # def print_stalls(i):
    #     print('Person {}: '.format(i), end='')
    #     for i in range(n + 2):
    #         if i in occupied_stalls:
    #             print('o', end='')
    #         else:
    #             print('.', end='')
    #
    #     print()

    for i_person in range(k):
        max_comfort__score = occupied_stalls[1] - occupied_stalls[0]
        max_comfort__i_stall_l = 0

        for i_stall_l in range(1, len(occupied_stalls) - 1):
            i_stall_r = i_stall_l + 1

            stall_l = occupied_stalls[i_stall_l]
            stall_r = occupied_stalls[i_stall_r]

            # The person contemplates entering the stall between stall_l and stall_r
            # Maximizing stall_r - stall_l is a sure way to pick a comfy loo.
            comfort_score = stall_r - stall_l

            if comfort_score > max_comfort__score:
                max_comfort__score = comfort_score
                max_comfort__i_stall_l = i_stall_l

        # Occupying the most comfortable stall:
        last_occupied_seat = occupied_stalls[max_comfort__i_stall_l] + (max_comfort__score // 2)
        i_last_occupied_seat = max_comfort__i_stall_l + 1
        occupied_stalls.insert(i_last_occupied_seat, last_occupied_seat)

    l_s = last_occupied_seat - occupied_stalls[i_last_occupied_seat - 1] - 1
    r_s = occupied_stalls[i_last_occupied_seat + 1] - last_occupied_seat - 1

    return max(l_s, r_s), min(l_s, r_s)


if __name__ == '__main__':
    num_test_cases = int(input())

    with open('output_c.txt', 'w') as f:
        for i_t in range(num_test_cases):
            n_, k_ = map(int, input().split(' '))
            max_, min_ = smart_solution(n_, k_)
            print('Case #{}: {} {}'.format(i_t + 1, max_, min_), file=f)
