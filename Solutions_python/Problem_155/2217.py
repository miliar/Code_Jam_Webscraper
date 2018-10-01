#!/usr/bin/python

import sys

def solve(input_file, output_file):
    num_cases = int(input_file.readline())
    for case_number in range(1, num_cases+1):
        max_shy, shy_str = input_file.readline().strip().split(' ')
        max_shy = int(max_shy)
        shy_list = [int(x) for x in shy_str]

        accumulated = 0
        invited = 0
        for i in range(0, max_shy+1):
            if i == 0:
                accumulated += shy_list[i]
            else:
                if accumulated < i:
                    invite = i - accumulated
                    invited += invite
                    accumulated += invite
                accumulated += shy_list[i]

        output_file.write("Case #%d: %d\n" % (case_number, invited))


if len(sys.argv) == 2:
    sys.argv.append(sys.argv[1] + '.out')
elif len(sys.argv) != 3:
    print "Invalid number of parameters. Call: %s input_file output_file" % sys.argv[0]
    exit(-1)

input_file = open(sys.argv[1])
output_file = open(sys.argv[2], 'w')

solve(input_file, output_file)

input_file.close()
output_file.close()
