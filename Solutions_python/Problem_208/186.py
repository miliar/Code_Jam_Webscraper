#!/usr/bin/python

from math import *

f=open('problem_3_small.in', 'r')
output=open('problem_3_small.out', 'w')

cases=int(f.readline())

def subtract_distance(horse, distance):
    return (horse[0],horse[1] - distance, horse[2])

def strictly_better(horse0, horse1):
    return horse0[1] > horse1[1] and horse0[2] > horse1[2]

def cant_make_it(horse, distance):
    return horse[1] - distance < 0

def small_answer(case, cities, horses, simple_routes):
    starter=subtract_distance(
        (0, horses[0][0], horses[0][1]), simple_routes[0])
    solutions=[(starter, [0])]
    for i in range(1, cities - 1):
        # print "i", i
        # print "solutions", solutions
        new_horse=(i, horses[i][0], horses[i][1])
        new_solutions=[]
        distance=simple_routes[i]
        # print "distance", distance
        # print "new_horse", new_horse
        for (current_horse, history) in solutions:
            # print "current_horse", current_horse
            if (cant_make_it(current_horse, distance)
                and cant_make_it(new_horse, distance)):
                # print 'x'
                x=0
            elif (cant_make_it(new_horse, distance)
                  or strictly_better(current_horse, new_horse)):
                chosen_horse=subtract_distance(
                    current_horse, distance)
                history.append(chosen_horse[0])
                new_solutions.append((chosen_horse, history))
            elif (cant_make_it(current_horse, distance)
                  or strictly_better(new_horse, current_horse)):
                chosen_horse=subtract_distance(
                    new_horse, distance)
                history.append(chosen_horse[0])
                new_solutions.append((chosen_horse, history))
            else:
                option1=subtract_distance(
                    current_horse, distance)
                option2=subtract_distance(
                    new_horse, distance)
                history2=history[:]
                history.append(option1[0])
                history2.append(option2[0])
                new_solutions.append((option1, history))
                new_solutions.append((option2, history2))
            solutions=new_solutions
    # print "solutions", solutions
    solution_times=[]
    for (_, history) in solutions:
        time=[]
        for (i,horse) in enumerate(history):
            distance=simple_routes[i]
            speed=horses[horse][1]
            time.append(float(distance) / speed)
        solution_times.append(sum(time))
    value=min(solution_times)
    # print "Case #%i: %s" % (case+1, value)
    output.write ("Case #%i: %s\n" % (case+1, str(value)))

for case in range(cases):
    arr=f.readline().replace("\n","").split(' ')
    cities=int(arr[0])
    pairs=int(arr[1])
    horses=[]
    for i in range(cities):
        arr=f.readline().replace("\n","").split(' ')
        distance=int(arr[0])
        speed=int(arr[1])
        horses.append((distance, speed))
    routes=[]
    for i in range(cities):
        arr=f.readline().replace("\n","").split(' ')
        routes.append([int(s) for s in arr])
    simple_routes=[ routes[i][i+1] for i in range(cities-1) ]
    trips=[]
    for i in range(pairs):
        arr=f.readline().replace("\n","").split(' ')
        start=int(arr[0])
        destination=int(arr[1])
        trips.append((start, destination))
    # print "cities", cities
    # print "horses", horses
    # print "simple_routes", simple_routes
    if pairs == 1:
        small_answer(case, cities, horses, simple_routes)
    # print ""
    # print ""
    # print "Case #%i: %s" % (case+1, value)
    # output.write ("Case #%i: %s\n" % (case+1, value))
    # output.write ("Case #%i: %s\n" % (case+1, str(value)))
