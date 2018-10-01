import sys


def check(num):
    num = str(num)
    for i in xrange(0,len(num)-1):
        # print i
        prev = num[i]
        nxt = num[i+1]
        # print "prev",prev,"nxt",nxt
        if nxt < prev:
            return False
    else:
        return True

sys.stdin = open("in","r")
T = int(input())
for count in xrange(T):
    num = int(raw_input())
    # num = 111111111111111110
    while True:
        res = check(num)
        if res is False:
            num -= 1
        else:
            break
    print "Case #{}: {}".format(count+1,num)
