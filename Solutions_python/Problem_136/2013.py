inputFile = open("input", "r")
outputFile = open("output", "w")
n_test_cases = inputFile.readline()
for case in range(int(n_test_cases)):
    values = inputFile.readline().rstrip().split(" ")
    c = float(values[0])
    f = float(values[1])
    x = float(values[2])
    initValue = x
    cps = 2.0
    sigValue = 0.0
    cost = 0.0
    while(initValue > sigValue):
        initValue = (x / cps) + cost
        cost = cost + c / cps
        cps = cps + f
        sigValue = (x / cps) + cost
    outputFile.write("Case #" + str(case + 1) + ": " + str(initValue) + "\n")
inputFile.close()
