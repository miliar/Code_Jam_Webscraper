data = open('B-small-attempt0.in')
tests = int(data.readline().strip())
for test in range(1, tests + 1):
    line = data.readline().strip()
    line = line.split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    time = X/2
    new_time = time
    N = 0
    rate = 2.0
    while new_time <= time:
        time = new_time
        N += 1
        new_time = 0
        rate = 2
        for i in range(N):
            new_time += C/rate
            rate += F
        new_time += X/rate
    print('Case #{0}: {1}'.format(test, time))
