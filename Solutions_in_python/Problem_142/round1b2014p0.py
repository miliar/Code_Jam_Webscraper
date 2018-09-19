import sys

T = int(sys.stdin.readline().rstrip())

for caseno in range(T):
    N = int(sys.stdin.readline().rstrip())

    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    def convert_to_powers(s):
        ret_val = []
        prev = s[0]
        cnt = 1
        for ch in s[1:]:
            if ch != prev:
                ret_val.append((prev,cnt))
                prev = ch
                cnt = 1
            else:
                cnt += 1
        ret_val.append((prev,cnt))
        return ret_val

    p1 = convert_to_powers(s1)
    p2 = convert_to_powers(s2)

    if len(p1) != len(p2):
        print "Case #%d: %s" % (caseno + 1, "Fegla Won")
        continue

    act = 0
    for i in range(len(p1)):
        if p1[i][0] != p2[i][0]:
            act = -1
            break
        else:
            act += abs(p1[i][1] - p2[i][1])

    if act < 0:
        print "Case #%d: %s" % (caseno + 1, "Fegla Won")
    else:
        print "Case #%d: %d" % (caseno + 1, act)
