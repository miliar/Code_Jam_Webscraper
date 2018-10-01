#!/usr/bin/python
#Problem 1: Saving the Universe

import sys

#infile = "test.in"
infile = "A-small-attempt1.in"
infile = "A-large.in"

#outfile= "test.out"
outfile = "A-small-attempt1.out"
outfile = "A-large.out"

try:
    f_in = open(infile)
except IOError:
    print infile, "can not be opened, plz check it out!"
    sys.exit(-1)
    
try:
    f_out = open(outfile,"w+")
except IOError:
    print outfile, "can not be opened, plz check it out!"
    sys.exit(-1)

# get the case num N
line = f_in.readline()
n_case = int(line)

for i in range(0,n_case):
    #get the num of engines
    line = f_in.readline()
    n_engine = int(line)
    l_engine = []
    
    #read the engines,put the name in l_engine, it's a list
    for j in range(0,n_engine):
        line = f_in.readline()
        l_engine += [line]
        
    #get the num of queries
    line = f_in.readline()
    n_query = int(line)
    flag_engine = [0 for x in range(0,n_engine)]
    n_marked = 0
    
    
    # find the engine which can handle the longest sequences, choose it
    # n_swith += 1
    j = 0
    n_swith = 0
    last_choose = -1
    while(j < n_query):
        
        # clear the flag of engines
        flag_engine = [0 for x in range(0,n_engine)]
        n_marked = 0
        if last_choose != -1:
            flag_engine[last_choose] = 1
            n_marked += 1
        last_choose = -1
        # check every query
        while (n_marked < n_engine) and (j < n_query):
            cur_query = f_in.readline()
            try:
                index = l_engine.index(cur_query)
            except ValueError:
                index = -1
                print "Query #", j+1, "of Case #",i+1, "is not the name of engines!!"
            if index!=-1 and flag_engine[index]!=1:
                print "Engine #", index, ":", l_engine[index],
                flag_engine[index]=1
                n_marked += 1
                last_choose = index
            j += 1
        
        if (n_marked == n_engine):
            print "Round Choose", j , l_engine[last_choose] 
            n_swith += 1
    #end all the queries of this case
    
    f_out.write("Case #"+ str(i+1) +": "+ str(n_swith) +"\n")
        
f_in.close()
f_out.close()