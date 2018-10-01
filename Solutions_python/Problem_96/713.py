#!/usr/bin/env python
'''
      
'''

import sys
from pprint import pprint

def do_one_case(csn,  N, S, p, l):
    ''' Not thoroughly debugged...'''
    googlers = 0
    for n in l:
        if n // 3  >  p-1:
            googlers += 1 
            #print "adding g for:", n
        if n // 3 == p-1 and n != 0:
            if n % 3 == 0:
                if S > 0:
                    S -= 1
                    googlers += 1 
                    #print "adding g for:", n, "costs a sup"
            else:
                googlers += 1 
                #print "adding g for:", n
        if n // 3 == p-2:
            if n % 3 == 2 and n != 0:
                if S > 0:
                    S -= 1 
                    googlers += 1 
                    #print "adding g for:", n, "costs a sup"

    print "Case #"+str(csn)+":", googlers 

def main():
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        line = sys.stdin.readline().strip().split()
        N = int(line[0])
        S = int(line[1])
        p = int(line[2])
        l = map(int, line[3:])
        #print W,H,T
        do_one_case(i+1, N, S, p, l)


if __name__ == "__main__":
    main()
