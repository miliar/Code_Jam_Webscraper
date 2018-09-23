#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def findMaxPosition(distance_list):
    """
    :input: list of int
    """
    length = len(distance_list)
    max_value = 0
    max_posision = 0
    for x in xrange(length):
        if distance_list[x] > max_value:
            max_value = distance_list[x]
            max_position = x
    return max_position

        

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    stalls = {}
    stalls[n] = 1
    max_distance = n
    max_pos = 0
    L_s = 0
    R_s = 0
    for person in xrange(k):
        #for key in sorted(stalls):
         #   print " %s: %s" % (key, stalls[key]) 
        #max_pos = findMaxPosition(stalls)
        max_distance = sorted(stalls.keys())[-1]
        L_s = (max_distance-1)/2
        R_s = max_distance/2
        if stalls.has_key(L_s):
            stalls[L_s] = stalls[L_s] + 1
        else:
            stalls[L_s] =  1

        if stalls.has_key(R_s):
            stalls[R_s] = stalls[R_s] + 1
        else:
            stalls[R_s] =  1

        if stalls[max_distance] == 1:
            del stalls[max_distance]
        else:
           stalls[max_distance] = stalls[max_distance] - 1

        if 0:
            print "person " + str(person) + "  list: " 
            #print stalls
            print str(max_distance)
            print "ans "+str(max(L_s, R_s))+ " "+str(min(R_s, L_s))


    print "Case #{}: {} {}".format(i, max(L_s, R_s), min(L_s, R_s))
    #print "Case #{}: {}".format(i, final_result)
    # check out .format's specification for more formatting options
