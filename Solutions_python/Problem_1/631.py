#!/usr/bin/env python

import sys
switch_counter = 0

def repeat(dct_queries, queries, servers_set):
    global switch_counter
    switch_counter += 1
    breaks = find_breaks(dct_queries)
    #print "Breaks:", breaks
    queries = part(queries, breaks)
    if not servers_set.issubset(set(queries)):
        print "Case #%s: %s" % ((case+1), switch_counter)
    else:
        repeat(find_posdict(queries), queries, servers_set)

def find_posdict(queries):
    dct_queries={}
    for pos,q in enumerate(queries):
        dct_queries.setdefault(q, []).append(pos)
    return dct_queries

def part(l, breaks):
    max = 0
    ret = []
    for pos, q in breaks:
        if q not in l[:pos]:
            t = len(set(l[:pos]))
            if t > max :
                ret = l[pos:]
                max = t
                #print "in Middle: ", ret
        if q not in l[pos+1:]:
            t = len(set(l[pos+1:]))
            if t > max:
                ret = l[:pos+1]
                max = t
                #print "in Middle: ", ret
    #print "See here:", ret
    return ret
            
def find_breaks(pos_dct):
    ret = []
    curr_min = 100
    for key, value in pos_dct.items():
        ret.extend([[item, key] for item in value])
    return ret


lines = file(sys.argv[1]).readlines()

num_of_cases = int(lines[0])

counter = 1
for case in range(num_of_cases):
    switch_counter = 0
    num_of_servers = int(lines[counter])
    servers=[]
    for server in range(num_of_servers):
        counter+=1
        servers.append(lines[counter].strip())
    #print servers
    servers_set = set(servers)
    counter+=1
    num_of_queries = int(lines[counter])
    queries=[]
    dct_queries={}
    for query in range(num_of_queries):
        counter+=1
        q = lines[counter].strip()
        if len(queries) == 0 or queries[-1] != q:
            queries.append(q)
            dct_queries.setdefault(q, []).append(len(queries)-1)
    counter+=1
    #print queries
    #print dct_queries
    queries_set = set(queries)
    if not servers_set.issubset(queries_set):
        print "Case #%s: %s" % ((case+1), 0)
    else:
        repeat(dct_queries, queries, servers_set)
    #print queries_set

