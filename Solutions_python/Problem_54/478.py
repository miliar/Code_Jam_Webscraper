lines = open('B-large.in', 'r').readlines()
out = open('B-large.out', 'w')

T = int(lines[0])
t = 1

def gcd(a, b):
    if b == 0 : return a
    return gcd(b, a % b)

while t <= T:
    
    line = lines[t]

    a = []
    
    start = 0
    while True:
        if line[start] == ' ':
            N = int(line[:start])
            break
        start = start + 1

    start = start + 1
    
    for i in xrange(N):
        j = start
        while True:
            if line[j] == ' ':
                a.append(int(line[start:j]))
                start = j + 1
            if line[j] == '\n':
                a.append(int(line[start:j]))
                break
            j = j + 1

    ans = abs(a[1] - a[0])

    for i in xrange(2, N):
        ans = gcd(ans, abs(a[i] - a[0]))

    out.write('Case #%d: ' % t)

    if a[0] % ans == 0 : out.write('0\n')
    else : out.write('%d\n' % (ans - (a[0] % ans)))

    t = t + 1
