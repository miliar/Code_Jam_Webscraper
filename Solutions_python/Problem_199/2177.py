def func(j, s, k):
    first = 0
    for i in xrange(int(k)):
        #print j, i, k
        try:
            if(s[j+i] == '-'):
                s[j+i] = '+'

            else:
                s[j+i] = '-'
                #happy = 0
                first = 1
        except:
            break

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input().split()
    k = s.pop()
    s = list(s[0])
    flip = 0
    happy = 1
    j = 0

    while j < len(s)-(int(k)-1):
        if s[j] == '-':
            flip += 1
            func(j, s, k)
        j+=1

    for j in s:
        if j == '-':
            happy = 0

    if happy != 0:
        print("Case #"+str(i)+": "+str(flip))
    else:
        print("Case #"+str(i)+": IMPOSSIBLE")


    #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
