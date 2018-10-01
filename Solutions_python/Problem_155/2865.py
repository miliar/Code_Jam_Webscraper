
def solve():
    s_max, s = raw_input().strip().split()
    extra_people = 0
    standing_people = int(s[0])
    for i in xrange(1, len(s)):
        diff = i - standing_people
        if diff > 0:
            standing_people += diff
            extra_people += diff
        standing_people += int(s[i])
    return extra_people


def main():
    n = input()
    for i in xrange(n):
        x = solve()
        print "Case #%s: %d" %((i+1), x) 

if __name__=='__main__':
    main()
