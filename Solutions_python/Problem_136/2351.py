import sys

if __name__ == '__main__':
    with open('input/bl') as input:
        for i in range(1, int(input.readline()) + 1):
            p = [float(x) for x in input.readline().split(' ')]
            elapsed = 0 ; gain = 2 ; cookies = 0
            while (True):
                time_to_buy_a_farm = p[0] / gain
                time_to_finish = p[2] / gain
                time_to_finish_with_new_farm = p[2] / (gain + p[1])
                time_to_finish_with_new_farm += time_to_buy_a_farm
                if time_to_finish > time_to_finish_with_new_farm:
                    gain += p[1]
                    elapsed += time_to_buy_a_farm
                else:
                    elapsed += time_to_finish
                    break
            print('Case #{:d}:'.format(i), elapsed)


