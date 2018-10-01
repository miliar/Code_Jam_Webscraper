from collections import Counter

def analyse(d, n, horses):

    horses = sorted(horses, key=lambda v : v[0], reverse=True)


    #print("")
    #print("START", d, n, horses)
    currentDistance = float('inf')
    currentSpeed = float('inf')

    for i, (ki, si) in enumerate(horses):

        if si <= currentSpeed:
            currentSpeed = si
            currentDistance = ki
        else:

            meetTime = (ki - currentDistance)/(currentSpeed - si)
            meetPosition = ki + meetTime*si

            if meetTime < 0:
                print("Error", d, n, horses)
            if meetPosition > d:
                currentDistance = ki
                currentSpeed = si

       # print(currentSpeed, currentDistance)

    finishTime = (d-currentDistance)/currentSpeed
    maxSpeed = d/finishTime

    #print(maxSpeed)

    return str(maxSpeed)
    

def run(name):
    lines = [l for l in open(name + ".in", mode='r')]
    m = int(lines[0])
    l = 1

    out = open(name + ".out",mode='w')
    for i in range(m):
        d, n = lines[l].rstrip().split(" ")
        d = int(d)
        n = int(n)

        horses = []
        for k in range(n):
            ki, si = lines[l+k+1].rstrip().split(" ")
            horses.append((int(ki), int(si)))

        l += n + 1

        answer = analyse(d, n, horses)
        out.write("Case #" + str(i+1) + ": " + answer + "\n")
    out.close()

run("A-large")
