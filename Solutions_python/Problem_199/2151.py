def compute(s, k):
    i = 0
    count = 0
    while i < len(s):
        if s[i] == '-':
            # Flip the next k chars
            for j in xrange(i, i + k):
                if j >= len(s):
                    # Going out of bound
                    return -1
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
            count += 1
            #  print s
        i += 1
    return count


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s, k = raw_input().split(" ")
    s = list(s)
    k = int(k)
    #  print s, k
    result = 'IMPOSSIBLE'
    count = compute(s, k)
    if count >= 0:
        result = count
    print "Case #{}: {}".format(i, result)
