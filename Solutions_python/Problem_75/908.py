#!/usr/bin/python

import sys

ipt = []
src = []


def read():
    return sys.stdin.readlines()

def test( inputstring ):
    inputlist = inputstring.split()
    combine_case_count = int( inputlist[0] )
    combine_case_list = inputlist[1:combine_case_count+1 ]
    idx = 0
    idx = combine_case_count + 1
    opposite_case_count = int( inputlist[idx] )
    opposite_case_list = inputlist[idx+1:idx+1+opposite_case_count]
    invoke_count = int( inputlist[-2] )
    invoke_string = inputlist[-1]
    current_elements = ''
    for invoke_idx in range( invoke_count ):
        current_elements = current_elements + invoke_string[ invoke_idx ]
        if len(current_elements) > 1:
            for combine_idx in range( combine_case_count ):
                if current_elements[-2:] == combine_case_list[ combine_idx ][:2] or current_elements[-2:] == combine_case_list[ combine_idx ][1::-1]:
                    current_elements = current_elements[:-2] + combine_case_list[ combine_idx][2]
                    break
            for opposite_idx in range( opposite_case_count ):
                if current_elements.find( opposite_case_list[opposite_idx][0] ) >-1 and current_elements.find( opposite_case_list[opposite_idx][1] ) >-1:
                    current_elements = ''
                    break

    current_elements_string = ''
    elements_len = len( current_elements )
    if elements_len > 0:
        for elements_idx in range( elements_len - 1):
            current_elements_string += current_elements[ elements_idx ] + ', '
        current_elements_string += current_elements[ elements_len - 1]
    return '[' + current_elements_string + ']'



def runtest():
    for x in range(cases):
        #TODO :implement test code
        inputstring = ipt[ x + 1 ][:-1]
        ret = test( inputstring )
        print "Case #" + str(x + 1) + ": " + ret

if __name__ == '__main__':
    ipt = read()
    cases = int( ipt[0] )
    runtest()



