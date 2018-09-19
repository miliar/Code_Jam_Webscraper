import sys
    
num_cases = int(sys.stdin.readline())
f = open('myfile2','w')

for n in range(0, num_cases):
    line = sys.stdin.readline()
    inputs = line.split()
    C = float(inputs[0])
    F = float(inputs[1])
    X = float(inputs[2])

    rate = 2.0

    prev_time = X/rate
    
    i = 1
    while True:
        time = 0
        rate = 2.0
        for j in range(0, i):
            t = C/rate
            rate += F
            time += t
        time += X/rate
        if time >= prev_time:
            break
        else:
            prev_time = time
            i += 1
    f.write("Case #" + str(n+1) + ": " + str(prev_time) + "\n")

