#!/usr/bin/python

import sys

#import psyco
#psyco.full()

def main():
    # Read in
    infile = open(sys.argv[1])
    numtests = int(infile.readline())
    for i in range(numtests):
        line = infile.readline().strip().split()
        numsteps = int(line[0])
        line = line[1:]
        
        time = 0
        # For each robot: pos and time of last activity
        robots = {"B":(1,0), "O":(1,0)}
        other_robot = {"B": "O", "O": "B"}
        for step in range(numsteps):
            which, button = line[:2]
            button = int(button)
            line = line[2:]
            pos, last_act = robots[which]
            to_move = abs(pos - button)
            if to_move == 0:
                # Already there, press button
                time += 1
            else:
                # Not there: if last_act is less than time, we could move
                if last_act < time:
                    to_move -= time - last_act
                    to_move = max(0, to_move)
                # Now move the rest, press button
                time += to_move + 1
            robots[which] = (button, time)

        print "Case #%d: %s" % (i+1, time)

if __name__ == "__main__":
    main()
