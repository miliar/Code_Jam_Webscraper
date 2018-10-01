#!/usr/bin/env python

import sys

def print_list(l):
    l = list(l)
    s = '['
    for i in xrange(0,len(l)):
        s+=l[i]
        if i != len(l)-1:
            s+=', '
    s+=']'
    return s

def magicka( base, nonbase, s):
    #print base, nonbase, s
    ret = []
    for x in s:
        if ret==[]:
            ret.append(x)
            continue
        else:
            # try to combine
            last = ret[-1]
            combine_into = None
            for comb in base:
                if (comb[0] == last and comb[1]==x) or (comb[0]==x and
                    comb[1]==last):
                   combine_into = comb[2]
                   break
            if combine_into is not None:
                #print "combine", last, "and", x, "into", combine_into
                ret[-1] = combine_into
                continue
            else:
                # try to clear list (if in nonbase) 
                clear = False
                for comb in nonbase:
                    if comb[0]==x:
                        non_compatible=comb[1]
                    elif comb[1]==x: 
                        non_compatible=comb[0]
                    else:
                        continue

                    for character in ret:
                        if character == non_compatible:
                            clear = True
                            break
                if clear:
                    #print "clear", ret, "(", x, "appears and doesn't fit with", non_compatible, ")"
                    ret = []
                    continue 
            # finally, append
            ret.append(x)
    return print_list(ret)
                    

def solve(case):
    case_split = case.split(" ")
    index = 0
    C = int(case_split[index])
    index += 1
    base_element_list = [case_split[i] for i in xrange(index,C+index)]
    index += len(base_element_list)
    D = int(case_split[index])
    index += 1
    non_base_element_list = [case_split[i] for i in xrange(index,D+index)]
    index += len(non_base_element_list)
    N = int(case_split[index])
    index += 1
    s = case_split[index] 
    return magicka(base_element_list, non_base_element_list, s) 

def parse_args():
    f = open(sys.argv[1]) 
    n = int(f.readline().strip())
   
    for i in xrange(1,n+1):
        case = f.readline().strip()
        print "Case #" + str(i)+ ":", solve(case)

parse_args()
