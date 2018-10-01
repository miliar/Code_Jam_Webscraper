#!/usr/bin/python

import sys
from collections import defaultdict

def parse_input(file_):
    with open(file_, 'r') as f:
        N = int(f.readline())
        with open(file_.replace("in", "out"), "a") as outfile:
            outfile.truncate(0)
        for case in range(1, N+1):
            line = f.readline()[:-1]
            X = int(line.split(" ")[0])
            R = int(line.split(" ")[1])
            C = int(line.split(" ")[2])

            # basic corner cases
            if X == 1 or R < 1 or C < 1:
                with open(file_.replace("in", "out"), "a") as outfile:
                    outfile.write("Case #" + str(case) + ": GABRIEL\n")
                continue

            # divisibility test
            if (R * C) % X != 0:
                with open(file_.replace("in", "out"), "a") as outfile:
                    outfile.write("Case #" + str(case) + ": RICHARD\n")
                continue

            # HITM test (i.e. Hole-In-The-Middle)
            if X >= 7:
                with open(file_.replace("in", "out"), "a") as outfile:
                    outfile.write("Case #" + str(case) + ": RICHARD\n")
                continue

            # Can Gabriel survive any L-shaped piece? (line-pieces included)
            done = False
            for i in range(0, X/2 + 1):
                if (i+1 > R and (X-i) > R) or (i+1 > C and (X-i) > C):
                    with open(file_.replace("in", "out"), "a") as outfile:
                        outfile.write("Case #" + str(case) + ": RICHARD\n")
                    done = True
                    break

            if done:
                continue

            # Can he survive a tough starting piece?
            if R > 1 and C > 1 and (R == X / 2 or C == X / 2):
                with open(file_.replace("in", "out"), "a") as outfile:
                    outfile.write("Case #" + str(case) + ": RICHARD\n")
                continue
            
            with open(file_.replace("in", "out"), "a") as outfile:
                outfile.write("Case #" + str(case) + ": GABRIEL\n")

parse_input(sys.argv[1])

