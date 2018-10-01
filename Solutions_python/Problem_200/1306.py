#!/usr/bin/python3

import getopt
import sys
import math

def is_tidy(X):
    """ returns 0 if tidy else index of violating element """
    
    last = '1'
    for i,x in enumerate(X):
        if x < last:
            return i 
        last = x
    return 0

def change_pos(X):

    pos = is_tidy(X)
    skip_to = len(X) - pos  
    cpos = 0
    
    last = '9'
    for i,e in enumerate(reversed(X)):
      if i < skip_to:
          last = e
          continue
      if e < last:
          cpos = len(X) - i 
          break
      last = e

    return cpos 

def update(X, pos):
    X[pos]= chr(ord(X[pos])-1)

    for i in range(pos+1, len(X)):
        X[i]='9'

if __name__ == "__main__":

    verbose = False
    fname = "input.txt"

    if sys.version_info[0] < 3:
        print("This script requires Python 3. (You are running %d.%d)" % (
            sys.version_info[0], sys.version_info[1])) 
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvf:",
                                   ["verbose","help","input="])
    except getopt.GetoptError as err:
        print (str(err)) 
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"): sys.exit()
        elif o in ("-v", "--verbose"): verbose = True
        elif o in ("-f", "--input"): fname = a
        else: sys.exit()

    f = open(fname, "rt")
    ncases = int(f.readline())

    for c in range(ncases):
        X = list(f.readline().strip())
        saved = list(X)

        if is_tidy(X) != 0 :
            cpos = change_pos(X)
            update(X,cpos)
        
        A = int("".join(X))
        B = int("".join(saved))

        if verbose:
            print("Case #%d: %d %d (%d diff)" % (c+1,B,A,A-B))
        print("Case #%d: %d" % (c+1,A))





        

        




