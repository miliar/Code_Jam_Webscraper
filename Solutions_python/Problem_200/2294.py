def is_increasing(n):
    s = str(n)
    last = int(s[0])
    for i in range(1, len(s)):
        if int(s[i]) < last:
            return False
        last = int(s[i])
    return True

def get_next(n):
    if is_increasing(n):
        return n
    while n % 10 != 9:
        n -= 1
    s = str(n)
    if len(s) == 1:
        return n
    pre = s[:-1]
    return int(str(get_next(int(pre))) + '9')

t = int(raw_input())
for q in range(t):
    n = int(raw_input())
    print "Case #%d: %d" % (q + 1, get_next(n))
