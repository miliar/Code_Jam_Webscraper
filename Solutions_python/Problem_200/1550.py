def is_tidy(n):
    # returns (True, 0) if tidy else (False, location of first untidy digit (left to right, count starts at 0) )
    s = '%d' % (n)
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            return False, i
    return True, 0


def solve(n):
    done, d = is_tidy(n)
    if done: return n
    
    s = '%d' % (n)
    s2 = []
    s2.append(s[:d-1])
    s2.append( str(int(s[d-1])-1) )
    for i in range(len(s[d:])):
        s2.append('9')
    
    n = int( ''.join(s2) )
    return solve(n)


t = int(raw_input())
for i in xrange(1, t+1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, solve(n))