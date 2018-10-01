#!/usr/bin/env python
#coding=utf-8

import math

# input 
infilepath = "A-large.in"
#infilepath = "sample.in"
#infilepath = "A-small-attempt0.in"
outfilepath = infilepath.replace(".in", ".out")

def do_case(infile):
    #parse
    P, K, L = map(int, infile.readline().strip().split())
    print P, K, L
    freq = map(int, infile.readline().strip().split())
    freq.sort()
    freq.reverse()
    print freq
    
    keypad = [ [] for i in range(K) ]
    print keypad
    
    m = 1
    for f in freq:
        print f
        
        found = False
        for k in keypad:
            if len(k) < m:
                k.append(f)
                m = len(k)
                found = True
                break;
    
        if found == False:
            keypad[0].append(f)
            m += 1
            
        print keypad
    
    click = 0;
    for k in keypad:
        factor = 1
        for n in k:
            click += n * factor
            factor += 1
            
    print click
    return str(click)

def main():
    ifobj = file(infilepath)
    ofobj = file(outfilepath, "w")
        
    num_of_case = int(ifobj.readline().strip())
    print int(num_of_case)
    
    for i in range(num_of_case):
        answer = do_case(ifobj)
        
        str1 = "Case #%d: %s" % (i+1, answer)
        print str1
        ofobj.write(str1)
        ofobj.write('\n')
        
    # release resource
    ifobj.close()
    ofobj.close()
    
if __name__ == "__main__":
    main()
