import sys
import os
import math

def decode(line):
    """decoder"""
    word_list = line.split()
    n = int(word_list[0])
    s = int(word_list[1])
    p = int(word_list[2])
    word_list = word_list[3:]
    
    out = 0
    
    for i in range(len(word_list)):
        total = int(word_list[i])
        if (math.floor(total/3.0 + 2/3.0) >= p):
            out += 1
        elif (s > 0 and math.floor(total/3.0 + 4/3.0) >= p and math.floor(total/3.0 - 2/3.0) >= 0):
            s -= 1
            out += 1
    return out

def main(f_path):
    """main"""
    file_object = open(f_path, 'r')
    
    num_cases = int(file_object.readline())
    for i in range(num_cases):
        line = file_object.readline()
        print 'Case #%i: %i' % (i+1, decode(line))

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])
        

        

            
    