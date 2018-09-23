# tidy_numbers.py

# NOTE: Attempt to scale for numbers of 10^18 (i.e., 18 digits)

import numpy as np
lines = open('B-large.in', 'r').read().splitlines()
cases = int(lines[0])


for number in range(cases):
    find_tidy = lines[number+1]
    while True:
        tidy_list = np.array(list(find_tidy))
        lenth = len(tidy_list)
        allNotSet = False
        for i in range(1, lenth):
            if not tidy_list[i-1] <= tidy_list[i]:
                tidy_list[i-1] = int(tidy_list[i-1]) - 1
                tidy_list[i:] = 9
                allNotSet = True
                find_tidy = list(tidy_list)
                break
        if not allNotSet:
            break
    print('Case #{}: {}'.format(number+1, int(''.join(tidy_list))))
