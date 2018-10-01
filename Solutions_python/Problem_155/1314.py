#!/usr/bin/env python

import sys

def read_input(filename):
    test_cases = []
    infile = open(filename)
    for i,line in enumerate(infile.readlines()):
        if i == 0:
            continue
        else:
            temp = line.rstrip().split()
            test_cases.append([int(temp[0]),temp[1]])
        
    infile.close()
    return test_cases
    
def determine_friends(case):
    max_j = case[0]
    if not(max_j):
        # no shy audience members -> who needs friends?
        return 0
    else:
        friends = 0
        n_clapping = 0 # number of people already clapping
        for i,n_i in enumerate(case[1]):
            if i == 0:
                n_clapping += int(n_i)
            else:
                if n_clapping >= i:
                    # enough people are clapping for the i-th lot to be happy
                    n_clapping += int(n_i)
                else:
                    # number of people required for group i to clap
                    req = i - n_clapping
                    # add friends
                    friends += req
                    n_clapping += req
                    n_clapping += int(n_i)
                    
    return friends 
    
def main(filename,outname):
    out_stream = open(outname,'w')
    test_cases = read_input(filename)
    
    for i,case in enumerate(test_cases):
        n_friends = determine_friends(case)
        out_stream.write('Case #%d: %d\n' % (i+1,n_friends))
        
    out_stream.close()
    
    print "Done"
    return
    
if __name__ == "__main__":
    in_name = sys.argv[1]
    out_name = sys.argv[2]
    main(in_name,out_name)
    
