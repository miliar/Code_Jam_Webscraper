def best_game(c, f, x):
    decreasing = True
    numFactories = 0
    times = []
    prevRun = 0
    prod = 2
    first = True
    while (decreasing):
        run = 0
        if first:
            first = False
        else:
            prevRun += c / prod
            prod += f
        run += (x / prod) + prevRun
        times.append(run)
        if len(times) > 1 and run > times[-2]:
            decreasing = False
        numFactories += 1
    return min(times)

t = int(raw_input())

for i in range(1, t+1):
    line = raw_input().split(" ")
    print "Case #" + str(i) + ": " + str(best_game(float(line[0]), float(line[1]), float(line[2])))
