'''
Created on Apr 13, 2012

@author: csalazar
'''
import sys

if __name__ == "__main__":
    f = sys.stdin
    
    n_tests = int(f.readline())
    for j in range(1, n_tests+1):
        n, m = [int(x) for x in f.readline().split(' ')]
        
        checked = []
        counter = 0
        rango = [str(x) for x in range(n, m+1)]
        for number in rango:
            for i in range(-1, -len(number), -1):
                new_number = number[i:] + number[:i]
                if (number != new_number) and (new_number in rango):
                    if (number, new_number) not in checked:
                        checked.append((number, new_number))
                        counter += 1
            
        print "Case #%d: %d" % (j, counter/2)