#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      gcj2015
#
# Author:      makwa python3
#
# Created:     11/04/2015
# Copyright:   (c) udonko 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
problemname="StandingOvation"

def resolve(maxnum, audiences):
    num_standing=0
    additonal_stand=0
    for index, num_audience in enumerate(audiences):
        if num_audience == 0:
            continue
        else:
            thistimeadd = 0
            if index > num_standing:
                thistimeadd = index - num_standing
                additonal_stand += thistimeadd
            num_standing += num_audience + thistimeadd
    return additonal_stand
def readfile_and_writefile(filename):
    with open(filename, "r") as inputfile:
        with open(problemname+"_out.txt", "w") as outputfile:
            num = int(inputfile.readline())
            for i in range(num):
                line = inputfile.readline().strip()
                a,b = line.split()
                maxlevel = int(a)
                audiences = [int(ch) for ch in b]
                result = resolve(maxlevel, audiences)
                text = "Case #{0}: {1}\n".format(i+1, result)
                outputfile.write(text)



def main():
    readfile_and_writefile(sys.argv[1])

if __name__ == '__main__':
    main()
