'''
Created on Apr 13, 2012

@author: csalazar
'''
import sys
import string

if __name__ == "__main__":
    google = string.maketrans("acbedgfihkjmlonpsrutwvyxqz", "yehosvcdxiulgkbrntjwfpamzq")
    f = sys.stdin
    
    n_tests = int(f.readline())
    
    for i in range(1, n_tests+1):
        ln = f.readline().strip('\n')
        print "Case #%d: %s" % (i, string.translate(ln, google))