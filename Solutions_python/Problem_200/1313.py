t = int(raw_input())  # read a line with a single integer
for x in xrange(1, t + 1):
    n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    a = str(int(n[0]))
    big = -1
    if(len(a)==1):
        print "Case #{}: {}".format(x, a)
        continue
    same_digit = 0
    for i in range(0, len(a)-1):
        if(i>0):
            if(a[i]!=a[i-1]):
                same_digit = i
        if(a[i]>a[i+1]):
            big = i
            break
    if(big==-1):
        print "Case #{}: {}".format(x, a)
        continue
    a_first = int(a[0:same_digit+1]) - 1
    a_end = "9" * (len(a)-same_digit-1)
    a_final = (str(a_first)+str(a_end)).lstrip("0")
    print "Case #{}: {}".format(x, a_final)





