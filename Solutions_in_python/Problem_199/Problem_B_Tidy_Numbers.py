T = input() + 1
T_count = 1;
while T > T_count:
    l = map(str,raw_input().split())
    n = int(l[1])
    l = l[0]
    chars = []
    size = 0
    result = 0
    for c in l:
        size += 1
        chars.append(c)

    index = 0

    while index < size:
        if chars[index] == '-':
            result += 1
            count = n
            if index + count > size:
                result = -1
                break
            c_index = index
            while count > 0:
                if chars[c_index] == '-':
                    chars[c_index] = '+'
                else:
                    chars[c_index] = '-'
                c_index += 1
                count -= 1
        index += 1

    if result == -1:
        print "Case #" + str(T_count) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(T_count) +": " + str(result)
    T_count += 1