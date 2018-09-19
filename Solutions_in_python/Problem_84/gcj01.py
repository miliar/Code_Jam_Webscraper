#!/usr/bin/env python

# Chuck norris gets reincarnated before he dies !

import sys
sys.setrecursionlimit(1000000) # this should be f*cking default parameter !

###############################################################################
#
#   The real stuff 
#
###############################################################################

def parse(f):
    n = int(f.readline().strip())
    for case in xrange(1,n+1):
        line = Line( f.readline().strip() ) 
        A = line.get_int()
        B = line.get_int()

        pic = []
        for i in xrange(0, A):
            line = []
            c = Line( f.readline().strip() )
            pic.append( list(c.get_str()) )
        solve(case, pic) 

def solve(case, pic):
    print case_str(case)
    
    for i,line in enumerate(pic):
        for j,c in enumerate(line):
            if c == '#':
                if i!=0 and j!=0 and pic[i-1][j-1]=='a' and pic[i][j-1]=='c' and pic[i-1][j]=='b':
                    pic[i][j] = 'd'
                elif i!=0 and pic[i-1][j]=='a':
                    pic[i][j] = 'c'
                elif j!=0 and pic[i][j-1]=='a':
                    pic[i][j] = 'b'
                else:
                    pic[i][j] = 'a' 

    for i,line in enumerate(pic):
        for j,c in enumerate(line):
            if c == 'a':
                if i+1 >= len(pic) or j+1>=len(line):
                    print "Impossible"
                    return
                if pic[i+1][j+1]!='d':
                    print "Impossible"
                    return
                if pic[i][j+1] != 'b':
                    print "Impossible"
                    return
                if pic[i+1][j] != 'c':
                    print "Impossible"
                    return
            if c == 'b':
                if i+1 >= len(pic) or j==0:
                    print "Impossible"
                    return
                if pic[i][j-1]!='a':
                    print "Impossible"
                    return
                if pic[i+1][j-1] != 'c':
                    print "Impossible"
                    return
                if pic[i+1][j] != 'd':
                    print "Impossible"
                    return
            if c == 'c':
                if i==0 or j+1>=len(line):
                    print "Impossible"
                    return
                if pic[i-1][j]!='a':
                    print "Impossible"
                    return
                if pic[i-1][j+1] != 'b':
                    print "Impossible"
                    return
                if pic[i][j+1] != 'd':
                    print "Impossible"
                    return
            if c == 'd':
                if i==0 or j==0:
                    print "Impossible"
                    return
                if pic[i-1][j-1]!='a':
                    print "Impossible"
                    return
                if pic[i-1][j] != 'b':
                    print "Impossible"
                    return
                if pic[i][j-1] != 'c':
                    print "Impossible"
                    return


                
    for line in pic:
        s = ""
        for l in line:
            if l=='a' or l=='d':
                s += '/' 
            elif l=='b' or l=='c':
                s += '\\'
            else:
                s += l
        print s

def wp( score, skip = -1 ):
    w = float(0)
    t = float(0)
    for i,c in enumerate(score):
        if i == skip:
            continue
        if c == '.':
            continue
        if c == '0':
            t += 1
        if c == '1':
            w += 1
            t += 1
    return w/t

def owp( scores, index ):
    OWP = float(0)
    score = scores[index]
    opponents = float(0)
    for i,c in enumerate(score):
        if i == index or c == '.':
            continue
        if c == '0' or c == '1':
            opponents += 1
            OWP += wp(scores[i], index)
    return OWP / opponents 

def oowp( score, OWP):
    OOWP = float(0)
    opponents = float(0)
    for i,c in enumerate(score):
        if c == '.':
            continue
        if c == '0' or c == '1':
            opponents += 1
            OOWP += OWP[i] 
    return OOWP / opponents 



###############################################################################
#
#   Arg parsing helpers
#
###############################################################################

def getln(f):
    return f.readline().strip()

def case_str(n):
    return "Case #" + str(n) + ": "

# object to quickly get stuff from a input line
class Line(object):
    def __init__(self, line):
        self.line = line 
        self.line_split = line.split(" ")
        self.index = 0

    def get_str(self):
        s = str( self.line_split[self.index] )
        self.index += 1
        return s 

    def get_int(self):
        n = int( self.line_split[self.index] )
        self.index += 1
        return n

    def get_int_list(self, size=None):
        if size is None:
            # first number is the size of the list
            size = int( self.line_split[self.index] )
            self.index += 1
        l = [int(self.line_split[i]) for i in xrange(self.index, self.index + size)]
        self.index += size 
        return l

    def get_str_list(self, size=None):
        if size is None:
            # first number is the size of the list
            size = int( self.line_split[self.index] )
            self.index += 1
        l = [self.line_split[i] for i in xrange(self.index, self.index + size)]
        self.index += size 
        return l

def handle_input(ifile):
    f = open(ifile) 
    parse(f)
    f.close()

# main code
if len(sys.argv) < 2:
    print "You may want to give me an input file, jackass ?"
    sys.exit(1)
handle_input(sys.argv[1])

