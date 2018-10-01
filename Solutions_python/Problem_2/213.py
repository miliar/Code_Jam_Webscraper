import re, sys

def to_mins(time_str):
    hours, mins = [int(t) for t in time_str.split(':')]
    return hours * 60 + mins

def parse_sched(lines):
    depart = []
    arrive = []
    for l in lines:
        d, a = [to_mins(t) for t in l.split()]
        depart.append(d)
        arrive.append(a)
    depart.sort()
    arrive.sort()
    return depart,arrive

def solve_loc_needs(T, departures, arrivals):
    needed = 0
    num_arrived = 0
    while departures:
        if len(arrivals) == 0:
            if len(departures) > num_arrived:
                needed += len(departures) - num_arrived
            break
        if arrivals[0]+T <= departures[0]:
            num_arrived += 1
            arrivals = arrivals[1:]
        else:
            if num_arrived > 0:
                num_arrived -= 1
            else:
                needed += 1
            departures = departures[1:]
    return needed

def parse_input():
    if len (sys.argv) < 2:
        print "Enter an input filename please"
        return
    inp = open (sys.argv[1])

    lines = [re.sub(r'[\n\r]','',l) for l in inp.readlines()]
    num_cases = int(lines[0])
    line_num = 1
    for case in xrange(num_cases):
        T = int(lines[line_num])
        line_num += 1
        NA, NB = [int(n) for n in lines[line_num].split()]
        line_num += 1
        DepartA, ArriveB = parse_sched(lines[line_num:line_num+NA])
        line_num += NA
        DepartB, ArriveA = parse_sched(lines[line_num:line_num+NB])
        line_num += NB
        A_needs = solve_loc_needs(T, DepartA, ArriveA)
        B_needs = solve_loc_needs(T, DepartB, ArriveB)
        print "Case #"+str(case+1)+":", A_needs, B_needs

parse_input()