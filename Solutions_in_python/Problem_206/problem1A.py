
import random
def get_remaining_distance(pos,goal):
    return goal - pos

def get_remaining_time(start,goal,speed):
    distance = get_remaining_distance(start,goal)
    return distance/speed

goal = 2525
rem_time = get_remaining_time(2400,goal,5)

print(rem_time)
print(goal/rem_time)
#horses = [(120,60),(60,90)]
horses = [(2400,5)]
def get_max_time(goal,horses):
    maxspeeds = []
    for start,maxspeed in horses:
        rem_time = get_remaining_time(start,goal,maxspeed)
        maxspeeds.append(goal/rem_time)
    maxspeeds.sort()
    return maxspeeds[0]

def stresstest(cases=100,maxn = 1000):
    for _ in range(cases):
        horses = []
        goal = random.randint(1,10000)
        for _ in range(maxn):
            horses.append((random.randint(0,goal-1),random.randint(1,100)))
        print(get_max_time(goal,horses))

# print(get_max_time(2525,horses))
# print(get_max_time(300,[(120,60),(60,90)]))
# print(get_max_time(100,[(80,100),(70,10)]))
# stresstest()
with open('alarge.in') as infile:
    with open('aoutlarge.out','w') as outfile:
        cases = int(infile.readline())
        for casenum in range(cases):
            goal, numhorses = [int(a) for a in infile.readline().split()]
            horses = []
            for _ in range(numhorses):
                startpos, horsespeed = [int(a) for a in infile.readline().split()]
                horses.append((startpos,horsespeed))
            outfile.write("Case #" + str(casenum+1) + ": " + str(get_max_time(goal,horses)) + "\n")