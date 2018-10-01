search = 'welcome to code jam'

for n in xrange(int(raw_input())):
    data = []
    for c in raw_input():
        if data or c == search[0]:
            data.append(c)
    data = ''.join(data)

    search_len = len(search)

    done = {}
    def finder(search_pos, data_pos):
        if search_pos >= search_len:
            return 1

        key = (search_pos, data_pos)
        if key in done:
            return done[key]

        to_find = search[search_pos]

        tail = data[data_pos:]
        pos = tail.find(to_find)
        sum = 0
        while pos != -1:
            sum += finder(search_pos + 1, data_pos + pos) % 10000
            pos = tail.find(to_find, pos + 1)

        sum %= 10000
        done[key] = sum
        return sum

    print 'Case #%d:' % (n+1), str(finder(0, 0)).rjust(4, '0')

