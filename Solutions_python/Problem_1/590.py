#!/usr/bin/python

import sys

#states are represented as ((switches so far), (queries left))

def expand(s):
    engines = ucs.engines
    if g(s) > 0:
        curr_eng = s[0][-1]
    else:
        curr_eng = ""
    children, switches = [], ()
    for engine in engines:
        if engine != curr_eng:
            switches = s[0]+(engine,)
            #do all queries we can for this engine
            if engine in s[1]:
                queries = s[1][list(s[1]).index(engine):]
            else:
                queries = ()
            children += [(switches, queries)]
    return children

def goal_test(s):
    return len(s[1])==0

def g(s):
    return len(s[0])

def ucs(expand, start, goal, g, e, unit = True):
    ucs.engines = e
    open_list = []
    closed_list = []
    curr = (start, 0)
    while not goal(curr[0]):
        if not curr[0][1:] in closed_list:
            closed_list += [curr[0][1:]]
            open_list += [(x, g(x)) for x in expand(curr[0])]
        if not len(open_list) == 0:
            curr = open_list.pop(0)
        else:
            return
    return curr

ucs.engines = None

def main():
    pass

def getline(infile):
    return infile.readline().strip()

def getint(infile):
    return int(getline(infile))

if __name__ == '__main__':
    infile = open(sys.argv[1])
    #loop for each test case
    for i in range(int(getint(infile))):
        engines = []
        #get search engines
        for e in range(getint(infile)):
            engines += [getline(infile)]

        queries = ()
        #get queries
        for q in range(getint(infile)):
            queries += (getline(infile),)

        print "Case", "#"+str(i+1)+":", max(0,ucs(expand, ((), queries), goal_test, g, engines)[1]-1)
