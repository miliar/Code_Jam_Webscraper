'''
Created on 2010/04/07

@author: exilis
'''
import sys,re,math
from multiprocessing import Pool

def task(args):

    testid, N, K = args
    light = "OFF"
    
    if (1<<N)-1 == (K & ((1<<N)-1)):
        light = "ON"
            
    return (testid,light)

def parse_test_cases(filename):
    lines = [i.strip() for i in open(filename, "r").readlines()]
    cur = 0
    
    for case in lines[1:]:
        fields = case.split(" ")
        N = int(fields[0])
        K = int(fields[1])
        cur += 1
        yield [cur, N, K]

def output_result(res):
    for i in res:
        print "Case #%d: %s" % i

if __name__ == '__main__':

    if 0:
        pool = Pool()
        result = pool.map(task,parse_test_cases(sys.argv[1]))
    else:
        result = [task(i) for i in parse_test_cases(sys.argv[1])]

    output_result(result)
