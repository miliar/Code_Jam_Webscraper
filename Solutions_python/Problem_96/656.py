import string

#fname = 'A-small'
fname = 'B-large'
f = open('/Users/evolz/codejam/%s.in' % fname, 'r')
lines = []
noc = 0 # no of cases
for line in f.readlines():
    lines.append(line)
noc = int(lines[0])
result = []
i = 1
for line in lines[1:]:
    numbers = line.split(' ')
    T, s, p = numbers[0:3]
    tlen = len(numbers) - 1
    temp = numbers[tlen]
    numbers[tlen] = temp.replace('\n', '')
    T = int(T)
    p = int(p)
    s = int(s)
    counter = 0
    low_total = (p - 1) * 3
    s_total = p + (p - 2) * 2
    for t in numbers[3:]:
        if low_total < int(t):
            counter += 1
        else:
            if s > 0 and s_total <= int(t) and t != '0':
                counter += 1
                s -= 1
    result.append('Case #%s: %s' % (i, counter))
    i += 1
f.close()

f = open('/Users/evolz/codejam/%s.out' % fname, 'w')
f.write(string.join(result, '\n'))
f.close()
print string.join(result, '\n')
