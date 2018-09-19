import resource
import sys
# Increase max stack size from 8MB to 512MB
#resource.setrlimit(resource.RLIMIT_STACK, (2**,-1))
sys.setrecursionlimit(10**6)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def simulate(time, cps, farm_cost, farm_cps, goal):
    goal_time = goal/cps
    farm_time = farm_cost/cps
    goal_time_post = goal/(cps + farm_cps)
    #print time, cps, goal_time, farm_time, goal_time_post, goal

    if goal_time <= farm_time + goal_time_post: return time + goal_time
    return min([simulate(time + farm_time, cps + farm_cps,
                         farm_cost, farm_cps, goal),
                goal_time + time])
    


f = open("B-small-attempt1.in", "r")
contents = filter(lambda l: len(l) > 0, f.read().split("\n"))
contents = map(lambda l: map(float, l.split()), contents)
#print contents[25:29]
plays = list(map(lambda (i, pl): (i+1, simulate(0, 2.0, *pl)), 
                 enumerate(contents[1:])))

print "\n".join(map(lambda p: "Case #{}: {}".format(*p), plays))
