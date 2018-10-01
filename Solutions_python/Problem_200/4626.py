t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())  # read a list of integers, 2 in this case
    ret = ""
    s = str(n)
    l = len(s)
    tidy = True

    if n < int("1"*l):
        print "Case #{}: {}".format(i, "9"*(l-1))
        continue


    count = 0

    for j in xrange(l-1):
        if s[j] <= s[j+1]:
            ret += s[j]
            if s[j] == s[j+1]:
                count += 1
            else:
                count = 0
        else:
            tidy = False
            ch = chr(ord(s[j])-1)
            if count == 0:
                ret += ch
            else:
                ret = ret[:len(ret)-count]
                for k in xrange(count):
                    ret += ch
            while len(ret) < l:
                ret += '9'
            print "Case #{}: {}".format(i, int(ret))
            break

    if tidy:
        print "Case #{}: {}".format(i, n)
