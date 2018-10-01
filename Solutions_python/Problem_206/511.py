def main():
    num_cases = int(input())
    for case_num in range(num_cases):
        params = input().split(' ')
        dest = int(params[0])
        num_horses = int(params[1])

        horses = []
        for horse_num in range(num_horses):
            pos_spd = input().split(' ')
            horses.append((int(pos_spd[0]), int(pos_spd[1])))

        max_ttd = 0
        for pos, speed in horses[::-1]:
            time_to_dst = (dest - pos) / speed
            if time_to_dst > max_ttd:
                max_ttd = time_to_dst

        max_speed = dest / max_ttd

        print('Case #{0}: {1:.6f}'.format(case_num + 1, max_speed))


main()
