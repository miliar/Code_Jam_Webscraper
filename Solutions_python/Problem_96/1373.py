#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import sys

def main():
    if len(sys.argv) != 2:
        print "Usage: %s [FILE]\n" % (sys.argv[0])
        exit()

    with open(sys.argv[1]) as input_file:
        t = int(input_file.readline())
        for i, line in zip(xrange(1, t + 1), input_file):
            data = line.split()
            n = int(data[0])
            s = int(data[1])
            p = int(data[2])
            #print n, s, p, data[3:]
            
            special_points = (p - 2) * 2 + p
            min_points = (p - 1) * 2 + p
            #print special_points, min_points

            googlers_above_p = 0
            for points in data[3:]:
                points = int(points)
                if points >= min_points:
                    googlers_above_p += 1
                elif points >= special_points and points > 1 and s > 0:
                    googlers_above_p += 1
                    s -= 1
            print "Case #%d: %d" % (i, googlers_above_p)

main()

