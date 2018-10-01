'''
    Google Code Jam 2013
    Problem C: Fair and Square
    
    @author: Masood Behabadi
'''

import math

data_file = "data/C-small-attempt2.in"

def find_fairsquare(a, b):
    total = 0
    
    range_max = int(math.floor(math.sqrt(int(b))))
    c = int(math.ceil(math.sqrt(int(a))))
    
    while c <= range_max:
        sc = str(c)
        if sc == sc[::-1]:
            sq = str(c ** 2)
            if sq == sq[::-1]:
                total += 1
        c += 1
    
    return total

if __name__ == '__main__':
    
    f = file(data_file, "r")
    
    ncase = int(f.readline())
    
    for c in xrange(ncase):
        print "Case #%s:" % (c + 1),
        
        lower, upper = f.readline().strip().split(" ")
               
        print find_fairsquare(lower, upper)
        
        