#!/usr/bin/env python

def read_file(filename):
    with open(filename) as f:
        line = f.readline()
        line = line[:-1]
        N = int(line)
        strings = []
        for i in range(N):
            line = f.readline()
            line = line[:-1]
            strings.append(line)
        return strings

def find_msgs(s):
    message = 'welcome to code jam'
    appears = {}
    for c in message:
        appears[c] = []
        pos = 0
        while 1:
            pos = s.find(c, pos)
            if pos == -1:
                break
            appears[c].append(pos)
            pos += 1
    nums = 0
    for index in appears['w']:
        nums += n_next(index, appears, message, 1)
    return nums

def n_next(index, appears, message, pos):
    if pos == len(message):
        return 1
    nums = 0
    for i in appears[message[pos]]:
        if i > index:
            nums += n_next(i, appears, message, pos + 1)
    return nums

            
if __name__ == '__main__':
    import sys
    strings = read_file(sys.argv[1])
    f = open('out', 'w')
    for i in range(len(strings)):
        n = find_msgs(strings[i])
        f.write('Case #' + str(i + 1) + ': ')
        if n < 10000:
            s = '%04d\n' % (n, )
        else:
            s = '%d\n' % (n % 10000, )
        f.write(s)
    f.close()
