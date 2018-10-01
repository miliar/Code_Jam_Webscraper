with open('in.txt') as f:
    f.readline()
    case = 0
    for line in f:
        case += 1

        line = line.strip()
        s = [int(i) for i in line]
        n = len(s)
        for i in range(n-1,0,-1):
            if s[i] < s[i-1]: #make 9s
                s[i-1] = s[i-1] - 1
                for j in range(i,n):
                    s[j] = 9
        if s[0] == 0:
            s = s[1:]
        ans = ''.join(map(str,s))

        print "Case #%d: %s" % (case, ans)
