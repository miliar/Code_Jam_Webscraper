
from itertools import ifilter

def first_method(mushrooms):
    cnt = 0
    prev = mushrooms[0]
    for i in xrange(1, len(mushrooms)):
        if prev > mushrooms[i]:
            cnt += prev-mushrooms[i]
        prev = mushrooms[i]
    return cnt


def second_method(mushrooms):
    def calculate_eaten_mushrooms(mushrooms, rate):
        cnt = 0
        m = 0
        for i in xrange(len(mushrooms)-1):
            x = mushrooms[i]
            if m > x:
                return -1
            if x < rate:
                cnt += x
                m = 0
            else:
                cnt += rate
                m = x - rate
        if m > mushrooms[-1]:
            return -1
        return cnt

    a, b = 0, 10001
    while b-a > 1:
        rate = (a+b)//2
        if calculate_eaten_mushrooms(mushrooms, rate) < 0:
            a = rate
        else:
            b = rate

    cnt = calculate_eaten_mushrooms(mushrooms, a)
    if cnt < 0:
        return calculate_eaten_mushrooms(mushrooms, b)
    else:
        return cnt

def solve(mushrooms):
    return first_method(mushrooms), second_method(mushrooms)

T = int(raw_input())
for t in xrange(1, T+1):
    raw_input()
    a, b = solve(map(int, raw_input().split()))
    print "Case #%d: %d %d" % (t, a, b)
