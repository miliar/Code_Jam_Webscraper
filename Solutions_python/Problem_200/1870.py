t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    ans = n
    if n < 10:
        ans = n
    else:
        s = str(n)
        l = len(s)
        for j in xrange(1, l):
            if s[j] < s[j-1]:
                ans = '9' * (l - j)
                decrease = True
                for j in xrange(j-1, -1, -1):
                    if decrease:
                        if j == 0:
                            c = chr(ord(s[j]) - 1)
                            if  c != '0':
                                ans = c + ans
                        else:
                            if s[j] ==  s[j-1]:
                                ans = '9' + ans
                            else:
                                c = chr(ord(s[j]) - 1)
                                ans = c + ans
                                decrease = False
                    else:
                        ans = s[j] + ans


                break



    print 'Case #{0}: {1}'.format(i+1, ans)
