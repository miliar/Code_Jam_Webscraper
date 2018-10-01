def solve(n):
    test = n
    n_size = len(n)
    while True:
        cursor = -1
        for i in range(n_size-1):
            if int(n[i]) > int(n[i+1]):
                cursor = i
                break
        if cursor == -1:
            if n[0] == '0':
                del n[0]
            return n
        else:
            n[cursor] = str(int(n[cursor])-1)
            for i in range(cursor+1, n_size):
                n[i] = '9'

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = list(str(raw_input()))
    res = solve(n)
    print "Case #{}: {}".format(i, ''.join(res))
