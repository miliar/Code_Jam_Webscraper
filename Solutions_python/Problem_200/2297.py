def compute(s):
    for i in xrange(len(s) - 1, -1, -1):
        #  print i
        if i == 0:
            break
        if s[i] >= s[i-1]:
            continue
        for j in xrange(i, len(s)):
            s[j] = 9
        if s[i-1] == 0:
            s[i-1] = 9
        else:
            s[i-1] -= 1
        #  print s
    return ''.join(map(str, s)).lstrip('0')


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = [int(x) for x in list(raw_input())]
    result = compute(s)
    print "Case #{}: {}".format(i, result)
