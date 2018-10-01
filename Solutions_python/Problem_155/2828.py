f = open('out', 'w')
lines = open('A-large.in')
#lines = open('small.in')

cases = int(lines.readline())
for _ in range(cases):
    s, cnt = 0, 0
    mx, sq = lines.readline().strip('\n').split(' ')

    for i in enumerate(sq):
        index, el = i[0], int(i[1])
            
        if el != 0 and s < index:
            cnt += index - s
            s += index - s
            
        s += el

        if s > mx:
            break

    f.write("Case #%d: %d\n" % (_ + 1, cnt))
f.close()