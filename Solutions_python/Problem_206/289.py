with open("A-large.in", "r") as inp:
    with open("A-large.out", "w") as outp:
        cases = int(inp.readline())
        for i in range(cases):
            distance, horses = [int(x) for x in inp.readline().split()]
            time = 0
            for j in range(horses):
                currdist, currsp = [int(x) for x in inp.readline().split()]
                currtime = (distance-currdist)/currsp
                if currtime > time:
                    time = currtime
            outp.write("Case #" + str(i+1) + ": " + str(distance/time) + "\n")
