t = int(input())  # read a line with a single integer
for ii in range(1, t + 1):
    input_array = input().split(" ")
    flipper_len = int(input_array[1])
    pancake_array = list(input_array[0])
    pancake_num = len(pancake_array)

    result = ''
    if len([v for v in pancake_array if v == '+']) == pancake_num:
        print("Case #%d: 0" % ii)
        continue

    flip_count = 0
    last_ind = 0
    stop = False
    while True:
        if stop:
            break
        # print(pancake_array)
        flip_remain = flipper_len
        for i in range(last_ind, pancake_num):
            if flip_remain == flipper_len and pancake_array[i] == '+' and i == pancake_num - 1:
                result = str(flip_count)
                stop = True
                break
            elif flip_remain == flipper_len and pancake_array[i] == '+':
                continue
            elif flip_remain == flipper_len and pancake_num < i + flipper_len:
                result = 'IMPOSSIBLE'
                stop = True
                break
            elif flip_remain == flipper_len:
                last_ind = i
                flip_count += 1
                flip_remain -= 1
                pancake_array[i] = '+'
            elif flip_remain == 0:
                break
            else:
                pancake_array[i] = '+' if pancake_array[i] == '-' else '-'
                flip_remain -= 1

    print("Case #%d: %s" % (ii, result))
