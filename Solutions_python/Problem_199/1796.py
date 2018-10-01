def solve(pancakes, flipper_size):
    counter = 0
    p_transform = [x == '+' for x in pancakes]
    i = 0
    p_len = len(pancakes)
    while i < p_len:
        if i+flipper_size == p_len:
            j = i
            while j < i+flipper_size-1:
                if p_transform[j] != p_transform[j+1]:
                    return 'IMPOSSIBLE'
                j += 1
            if not p_transform[j]:
                counter += 1
            return counter
        if p_transform[i]:
            i += 1
            continue
        j = i+1
        while j < i+flipper_size:
            p_transform[j] = not p_transform[j]
            j += 1
        counter += 1
        i += 1
    return counter

for i in range(int(raw_input())):
    l = raw_input()
    pancakes, flipper_size = l.split(' ')
    result = solve(pancakes, int(flipper_size))
    print 'Case #%d: %s' % (i+1, result)