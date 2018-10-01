# need c cookies to buy a farm
# get f cookies/second upgrade rate
# x = goal
testcases = int(input())
for z in range(testcases):
    values = input().split(' ')
    c = float(values[0])
    f = float(values[1])
    x = float(values[2])
    p = 2
    t = 0
    while True:
        time_with_buy =  (c / p) + (x / (p+f))
        time_without_buy = (x / p)
        if time_with_buy < time_without_buy:
            t = t + c / p
            p = p + f
        else:
            t = t + x / p
            break
    print('Case #%d: %.7f' % ((z+1),t))