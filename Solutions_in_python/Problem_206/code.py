import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

inp = open("inal.in","r")
out = open("outal.out","w")
cases = int(inp.readline())
for casenum in range(1,cases+1):
    parse = inp.readline().split(" ")
    distance = int(parse[0])
    horses = int(parse[1])
    road = []
    maxtime = 0
    for horse in range(horses):
        y = inp.readline().split(" ")
        timetaken = (distance-int(y[0]))/int(y[1])
        if timetaken >= maxtime:
            maxtime = timetaken
    speed = distance/maxtime
    out.write("Case #{}: {}\n".format(casenum,speed))
    

inp.close()
out.close()
