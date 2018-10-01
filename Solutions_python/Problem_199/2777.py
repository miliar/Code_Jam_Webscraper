def flip(row, index, k):
    i = index
    if (index + k) > len(row):
        index = len(row) - k - 1
    for i in xrange(index, index + k):
        original = row[i]
        row[i] = (original + 1) % 2

def solve(row, k):
    flip_count = 0
    for index in xrange(len(row)):
        el = row[index]
        if el == 0:
            flip(row, index, k)
            flip_count += 1

    for el in row:
        if el == 0:
            return -1
    else:
        return flip_count

t = int(raw_input())

for case in xrange(t):
    line = raw_input().split(' ')
    k = int(line[-1])
    row = []
    for el in line[0]:
        value = 0 if el == '-' else 1
        row.append(value)

    count =solve(row, k)
    if count == -1:
        print 'case #{}: IMPOSSIBLE'.format(case+1)
    else:
        print 'case #{}: {}'.format(case+1, count)
