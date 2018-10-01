import sys, math

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for case in xrange(cases):
    smax, digits = stdin.pop(0).split(' ')
    smax = int(smax)
    digits = digits.strip()
    sum_ = 0
    friends = 0
    for i in xrange(len(digits)):
        digit = int(digits[i])
        if digit == 0:
            continue
        if friends+sum_ < i:
            friends += i - sum_ - friends
        sum_ += digit
    print "Case #"+str(case+1)+": "+str(friends)
