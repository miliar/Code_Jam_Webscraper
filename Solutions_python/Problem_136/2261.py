#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()
    
    for caseNr in xrange(1, testcases+1):
        cookierate = 2
        specline = raw_input()
        specs = specline.split()
        c = float(specs[0])
        f = float(specs[1])
        x = float(specs[2])
        farm = 0
        
        answer = x/cookierate
        oldanswer = answer
        
        while answer <= oldanswer:
            farm += c/cookierate
            cookierate += f
            oldanswer = answer
            answer = x/cookierate+farm    
        
        print("Case #%i: %.7f" % (caseNr, oldanswer))