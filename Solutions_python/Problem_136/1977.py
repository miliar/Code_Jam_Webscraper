import time

def solve(farmcost, farmincome, x):
    global wfile
    global case

    # We first detect raw length of time for c to reach x.
    timeRaw = x / 2

    lastTime = timeRaw
    # Now we can repeatedly add farms until we find the minimum point
    factories = 0
    factoriesTime = 0
    
    while True:
        incomesecond = 2 + (factories * farmincome)
        factoriesTime += farmcost / incomesecond
        factories += 1
        incomesecond = 2 + (factories * farmincome)
        newtime = ((x) / (incomesecond)) + factoriesTime

        if newtime < lastTime:
            lastTime = newtime
        else:
            break
    
    ans = lastTime

    wfile.write("Case #{0}: {1}\n".format(case, ans))
    case += 1


fle = open("input.in")
fle.readline()

case = 1

wfile = open("output.out", "w")

line = fle.readline()
while line != "":
    args = line.split(" ")
    c = float(args[0])
    f = float(args[1])
    x = float(args[2])
            
    solve(c, f, x)
    
    line = fle.readline()
