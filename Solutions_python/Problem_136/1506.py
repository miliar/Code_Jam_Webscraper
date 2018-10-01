f = open('B-large.in', 'r')
num = int(f.readline())
for x in range(0, num):
    values = f.readline().split()
    C = float(values[0])
    F = float(values[1])
    X = float(values[2])
    cps = 2.0
    seconds = X/cps
    while True:
        new_seconds = seconds - X/cps + C/cps
        cps += F
        new_seconds += X/cps
        if(seconds<new_seconds):
            break
        seconds = new_seconds
    print "Case #" + str(x+1) + ": " + '%.7f' % seconds
    
