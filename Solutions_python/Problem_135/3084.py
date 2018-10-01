import sys

lines = []
for line in sys.stdin.readlines():
    lines.append(line)

tc = int(lines[0])
del lines[0]

for i in range(1, tc+1):
    first = int(lines[0])
    f_row = set(int(x) for x in lines[first].split(' '))
    del lines[0:5]
    second = int(lines[0])
    s_row = set(int(x) for x in lines[second].split(' '))
    del lines[0:5]
    test = f_row.intersection(s_row)
    if not test:
        print 'Case #{}: Volunteer cheated!'.format(i)
    elif len(test) > 1:
        print 'Case #{}: Bad magician!'.format(i)
    else:
        print 'Case #{}: {}'.format(i, test.pop())
