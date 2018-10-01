case = input()
for x in xrange(0,case):
    cnt = 0;
    add = 0;
    level = raw_input().split()
    for i in xrange(0, int(level[0])+1):
        if int(level[1][i]) == 0:
            cnt += int(level[1][i])
            continue;
        if cnt < i:
            add += i-cnt
            cnt += add
        cnt += int(level[1][i])
    print "Case #"+str(x+1)+":", add
