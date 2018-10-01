#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def main():
    t = raw_input()
    for i in xrange(int(t)):
        ans = 0
        ss = 0
        k,l = raw_input().split(" ")
        for j in xrange(int(k) +1):
            if ss < j:
                ans += j - ss
                ss += j - ss
                
            ss += int(l[j]) 
        print "Case #{}: {}".format(i+1,ans)

if __name__ == "__main__":
    main()
