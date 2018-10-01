fin = open('A-large.in', 'r')
fout = open('out.txt', 'w')
t = int(fin.readline())
for cc in range(1, t + 1):
    n, x = map(int, fin.readline().split())
    s = [int(y) for y in fin.readline().split()]
    s.sort()
    result = 0
    while len(s) > 0:
        largest = s.pop()
        if len(s) > 0 and largest + s[0] <= x:
            s.pop(0)
        result += 1
    fout.write('Case #%d: %d\n' % (cc, result))
fin.close()
fout.close()
