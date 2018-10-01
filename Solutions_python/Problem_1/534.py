#!/usr/bin/env python

import sys

def parse_input(input):
    attrs = {}
    input = input.split("\n")
    attrs["test_cases"] = int(input[0].strip())
    i = 1
    tc = 0 # Current test case
    while True:
        tc += 1
        amount_se = int(input[i].strip())
        i += 1
        se_names = [name.strip() for name in input[i:i+amount_se]]
        i += amount_se
        amount_qu = int(input[i])
        i += 1
        queries = [q.strip() 
                    for q in input[i:i+amount_qu]]
        i += amount_qu
        attrs[tc] = {"names" : se_names,
                     "queries": queries}   
        if len(input) == i + 1:
            break
    return attrs

def get_last_matching(tc, qry_index_from, se_ignore):
    qrys = tc["queries"][qry_index_from:]
    # If the selection of a search engine doesn't need any switch
    # the system choose that one
    for se in tc["names"]:
        if se != se_ignore and se not in qrys:
            return se, len(tc["queries"]), False
    last_found = None
    qi = qry_index_from 
    ignore_list = [se_ignore] 
    for i, q in enumerate(qrys):
        if q in tc["names"] and q not in ignore_list:
            last_found = q
            qi = qry_index_from + i
            ignore_list.append(q)
    return last_found, qi, True 

def get_strategy(input_attrs):
    switch_order = []
    for i in xrange(input_attrs["test_cases"]):
        tc = i + 1
        qi = 0
        tc_so = []
        switches = 0
        name = ""
        while qi < len(input_attrs[tc]["queries"]):
            name, qi, switch = get_last_matching(input_attrs[tc], qi, name)
            qi += 1
            if name is None:
                break
            if switch:
                switches += 1
            tc_so.append(name)
        # Only to complete the strategy
        for se in input_attrs[tc]["names"]:
            if se not in tc_so: tc_so.append(se)
        # The last item of the strategy is the number of switches        
        tc_so.append(switches)
        switch_order.append(tc_so)

    return switch_order

def main(input):
    input_attrs = parse_input(input)
    strategy = get_strategy(input_attrs)
    for tc, strategy in enumerate(strategy):
        print "Case #%d: %d" % (tc+1, strategy[-1])
    
if __name__ == '__main__':
    input = open(sys.argv[1], "r").read()
    main(input)
