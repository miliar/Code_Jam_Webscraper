for tc in range(1, int(raw_input())+1):
    s = list(raw_input())
    p = 0
    i = 0
    while i < len(s):
        if p > s[i]:
            s[i] = chr(ord(s[i])-1)
            j = i
            while j > 0 and s[j-1] > s[j]:
                s[j] = '9'
                s[j-1] = chr(ord(s[j-1])-1)
                j -= 1
            while i < len(s):
                s[i] = '9'
                i += 1
            break
        else:
            p = s[i]
        i += 1
    print "Case #%d: %d" % (tc, int(''.join(s)))
