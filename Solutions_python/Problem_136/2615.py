t = input()
for i in range(t):
    r = 2
    c,f,x = map(float,raw_input().split())
    p = x/2
    temp = 0
    t = x/2
    while p >= t:
        p = t
        t = c/r + x/(r+f) + temp
        temp = c/r + temp
        r = r + f
    print p
