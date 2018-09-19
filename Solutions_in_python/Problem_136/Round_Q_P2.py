filename = raw_input()
fp = open(filename + '.in', 'r')
wfp = open(filename + '.out', 'w')
for it in range(int(fp.readline())):
    [C, F, X] = map(lambda x: float(x), fp.readline().split(' '))
    rate = 2.0
    t = 0.0
    while (C / rate + X / (rate + F)) < (X / rate):
        t += C / rate
        rate += F
    t += X / rate
    wfp.write('Case #' + str(it+1) + ': ' + str(t) + '\n')