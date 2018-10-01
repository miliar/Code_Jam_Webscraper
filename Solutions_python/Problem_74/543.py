#!/usr/bin/env python

infile = "A-large.in"
#infile = "A-small-attempt1.in"
#infile = "A-sample.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    ops = [value for value in fsrc.readline().split()]
    N = int(ops.pop(0))
    
    total_time = 0
    time = {'O': 0, 'B': 0}
    pos = {'O': 1, 'B': 1}
    for i in range(N):
        #print "Time:", time
        #print "Pos:", pos

        robot = ops[i*2]
        another_robot = 'O'
        if robot == another_robot:
            another_robot = 'B'

        op = int(ops[i*2+1])
        move_time = abs(pos[robot] - op)
        pos[robot] = op


        #print "Op:", robot, op

        if move_time > time[robot]:
            move_time -= time[robot]
        else:
            move_time = 0
        time[robot] = 0
        
        #print "Move time:", move_time
        total_time += move_time + 1
        time[another_robot] += move_time + 1

    res = "Case #%s: " %(t+1, ) 
    res += str(total_time) + '\n'
    print res,
    fres.write(res)

fsrc.close()
fres.close()
