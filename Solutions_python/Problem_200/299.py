infile = open('B-large.in', 'r')
outfile = open('tidy.out', 'w')

T = int(infile.readline())

for t in range(1, T + 1):
    N = infile.readline().strip()

    l = len(N)
    res = -1

    if l == 1:
        res = N
    elif int('1' * l) > int(N):
        res = '9' * (l - 1)
    else:
        res = int('1' * l)
        while l > 0:
            if res % 10 == 9:
                break
            adder = int('1' * l)
            if res + adder > int(N):
                l -= 1
            else:
                res += adder
    outfile.write('Case #{0}: {1}'.format(t, res) + '\n')
