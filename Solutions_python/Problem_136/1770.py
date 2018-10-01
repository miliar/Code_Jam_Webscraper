#/usr/bin/python
# Author: Cagil Ulusahin
# Date: 12 April 2014

import sys

def main(argv):
    if(len(argv) > 0):
        infile = argv[0]
    readFile(infile)


def readFile(infile):
    with open(infile) as f:
        T = int(f.readline())
        for t in range(0,T):
            row = get_row(f)
            answer = min_seconds(row)

            #print answer
            #print row1,row2
            print("Case #%d: %.7f" % (t+1,answer))

def min_seconds(row):
    c = row[0]
    f = row[1]
    x = row[2]
    old_min = x
    factory = 0
    new_min = x/2
    while(old_min > new_min):
        old_min = new_min
        factory += 1
        new_min = with_n_factory(c,f,x,factory)
    return old_min

def with_n_factory(c,f,x,factory):
    cook_per_sec = 2
    spent = 0
    for time in range(0,factory):
        spent += c/cook_per_sec
        cook_per_sec += f
    spent += x/cook_per_sec
    return spent

def get_row(f):
    line = f.readline().strip("\n").split(" ")
    row = [float(num) for num in line]
    return row

if __name__ == "__main__":
    main(sys.argv[1:])
