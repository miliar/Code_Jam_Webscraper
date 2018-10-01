#!/usr/bin/python

import sys

infile = "test.in"
infile = "B-small-attempt1.in"
infile = "B-large.in"

outfile = "test.out"
outfile = "B-small-attempt1.out"
outfile = "B-large.out"

try:
    f_in = open(infile)
except IOError:
    print infile, "can not be opened, plz check it out"
    sys.exit(-1)
    
try:
    f_out = open(outfile,"w+")
except IOError:
    print outfile, "can not be opened, plz check it out"
    sys.exit(-1)

line = f_in.readline()
N = int(line)

for i in range(0,N):
    # time around
    ta = int(f_in.readline())
    line = f_in.readline().split()
    NA = int(line[0])
    NB = int(line[1])
    
    
    la = []
    lb = []
    # read the start time and arrive time of A,B
    # store them in the list as (start_time, arrive_time)
    for k in range(0,2):
        if k==0:
            loop_time = NA
        else:
            loop_time = NB
        for j in range(0,loop_time):
            line = f_in.readline().split()
            s_start = line[0].split(':')
            s_arrive = line[1].split(':')
            i_start = int(s_start[0])*60 + int(s_start[1])
            i_arrive = int(s_arrive[0])*60 + int(s_arrive[1])
            if k==0:
                la.append((i_start,i_arrive))
            else:
                lb.append((i_start,i_arrive))
#    print la,lb
    
    num_A = NA
    num_B = NB    
    # Step1: sort A according arrive_time asc
    #        sort B according start_time asc    
    sort_A = sorted(la, key=lambda x:x[1])
    sort_B = sorted(lb, key=lambda x:x[0])
    
    j = k = 0
    while j<NA and k<NB:
        if sort_A[j][1] + ta <= sort_B[k][0]:
            num_B -= 1
            j+=1
#            print "A",j+1,"->B",k+1
        k+=1
    
    # Step2: sort B according arrive_time asc
    #        sort A according start_time asc    
    sort_B = sorted(lb, key=lambda x:x[1])
    sort_A = sorted(la, key=lambda x:x[0])
    
    j = k = 0
    while j<NB and k<NA:
        if sort_B[j][1] + ta<= sort_A[k][0]:
            num_A -= 1
            j+=1
#            print "B",j+1,"->A",k+1
        k+=1            
    
#    print num_A, num_B
    f_out.write("Case #"+ str(i+1) +": " + str(num_A) + " " + str(num_B) + "\n")
f_in.close()
f_out.close()


