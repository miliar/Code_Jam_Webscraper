import sys
def stan_ova(smax,s):
    count = s[0]
    friends = 0
    for i in xrange(1,smax+1):
        if s[i] != 0:
            tmp = i - count
            if tmp > 0:
                friends += tmp
                count += s[i] + tmp
            else :
                count += s[i]
    return friends

f = open('A-large.in','r')
f1 = open('output1.txt','w')
tc = int(f.readline())
for i in xrange(tc):
    s = f.readline().split()
    smax = int(s[0])
    shy_l = map(int,list(s[1]))
    f1.write("Case #%d: %d\n" %(i+1,stan_ova(smax,shy_l)))
f.close()
f1.close()
