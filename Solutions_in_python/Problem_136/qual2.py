def cookies(c, f, x, factor=2):
    totalTime = 0
    while True:
        time_to_win = x/factor
        farm_time = c/factor
        time_to_win_with_farm = x/(factor+f)
        result = farm_time + time_to_win_with_farm
        if time_to_win < result:
            return totalTime + time_to_win
        totalTime += farm_time
        factor += f

with open('B-large.in') as f, open('result.txt', 'w') as w:
    num = int(f.readline().strip())
    count = 1
    print num

    for line in f:
        args = [float(x) for x in line.strip().split()]
        ans = cookies(args[0], args[1], args[2])
        w.write("Case #%d: %.7f\n" % (count, ans))
        count += 1
    
