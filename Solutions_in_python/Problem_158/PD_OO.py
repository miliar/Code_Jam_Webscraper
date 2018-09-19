#!/usr/bin/python
import sys
import inspect

def linno():
    return inspect.currentframe().f_back.f_lineno

def do_each_case():
    Line = f.readline().rstrip("\n").strip(' ').split(" ")
    X = int(Line[0])
    R = int(Line[1])
    C = int(Line[2])
    if debug: print "=================="
    if debug: print X,R,C

    if X > R and X > C:
        if debug: print "hit@ %d" %(linno())
        return "RICHARD"

    if  not R*C % X == 0:
        if debug: print "hit@ %d" %(linno())
        return "RICHARD"

    if X == 1 or X ==2 :
        if debug: print "hit@ %d" %(linno())
        return "GABRIEL"

    if X == 3:
        if (R == 1 or C == 1):
            if debug: print "hit@ %d" %(linno())
            return "RICHARD"
        else:
            return "GABRIEL"
    if X == 4:
        if (R == 1 or C == 1):
            if debug: print "hit@ %d" %(linno())
            return "RICHARD"
        elif (R == 2 or C == 2):
            if debug: print "hit@ %d" %(linno())
            return "RICHARD"
        elif (R == 3 or C == 3):
            if debug: print "hit@ %d" %(linno())
            return "GABRIEL"
        else:
            return "GABRIEL"

    return "RICHARD"

if (len(sys.argv) == 3 and sys.argv[2] == "-d"):
    debug=True
else:
    debug=False

filename=sys.argv[1]

f=open(filename,'r')

CaseNum = int(f.readline().strip("\n"))
for c in range(1,CaseNum+1):
    ret = do_each_case()
    if ret == None:
        raise(Exception("no result"))
        
    print "Case #%d: %s" % (c ,ret)

