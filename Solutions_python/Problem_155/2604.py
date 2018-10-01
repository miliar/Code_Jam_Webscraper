T = raw_input()
T = int(T)

for i in range(T):
    Smax,Slist = raw_input().split(' ');
    Smax = int(Smax)
    People_Standing = 0
    Friends_to_invite = 0
    for j in range(Smax+1):
        if People_Standing >= j:
            People_Standing = People_Standing + int(Slist[j])
        else:
            Friends_to_invite = Friends_to_invite + 1
            People_Standing = People_Standing + 1 + int(Slist[j])
    print "Case #" + str(i+1) + ": " + str(Friends_to_invite)
