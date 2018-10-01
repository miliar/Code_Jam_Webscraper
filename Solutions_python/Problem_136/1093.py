T = int(raw_input())

for i in xrange(T):
    C, F, X = map(float, raw_input().split())
    production = 2
    time = X / production
    while(1):
        new_time = time - X / production + X / (production + F) + C / (production)
        if new_time >= time:
            print 'Case #%d: %.7f' %(i+1, time)
            break
        time = new_time
        production += F
