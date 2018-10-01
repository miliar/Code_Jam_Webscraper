import heapq
t = int(raw_input()) 
for i in xrange(1, t + 1):
    stalls, users = [int(elem) for elem in raw_input().split(' ')]
    levels = [{stalls : 1}]
    n = users
    while True:
        old_level = levels[-1]
        new_level = {}
        for el in old_level:
            if el == 0:
                continue
            if el % 2 == 1:
                new_level[el / 2] = new_level.get(el / 2, 0) + 2 * old_level[el]
            else:
                new_level[(el - 1) / 2] = new_level.get((el - 1) / 2, 0) + old_level[el]
                new_level[(el - 1) / 2 + 1] = new_level.get((el - 1) / 2 + 1, 0) + old_level[el]
        levels.append(new_level)
        if len(new_level) == 1 and 0 in new_level:
            break
    for j in range(len(levels)):
        summ = 0
        for key in levels[j]:
            if key != 0:
                summ += levels[j][key]
        if users > summ:
            users -= summ
            continue
        items = sorted(levels[j].items(), key = lambda x : -x[0])
        for elem in items:
            if elem[1] >= users:
                users -= elem[1]
                user_pos = elem[0] / 2
                ls = user_pos
                rs = elem[0] - user_pos - 1
                print "Case #{}: {} {}".format(i, max(ls, rs), min(ls, rs))
                break
            else:
                users -= elem[1]
        if users <= 0:
            break