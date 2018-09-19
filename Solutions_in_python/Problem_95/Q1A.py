#!/usr/bin/env python

import sys
import re

def main():
    input_file = open(sys.argv[1], "r")
    
    cases = input_file.readline()
    strings = []
    for line in input_file:
        strings.append(line)
        
    input_file.close()
    
    sentences = []
    for s in strings:
        temp = []
        temp = s.split(" ")
        sentences.append(temp)
    
    output_file = open("output.txt", "w")
    
    mapping = {'e':'o', 'y':'a', 'q':'z', 'j':'u', 'p':'r', 'm':'l', 's':'n', 'l':'g', 'c':'e', 'k':'i', 'd':'s', 'x':'m', 'v':'p', 'n':'b', 'r':'t', 'i':'d', 'b':'h', 't':'w', 'a':'y', 'h':'x', 'w':'f', 'f':'c', 'o':'k', 'u':'j', 'g':'v', 'z':'q'}
    
    case_num = 1
    for s in sentences:
        case_header = "Case #" + str(case_num) + ": "
        sys.stdout.write(case_header)
        output_file.write(case_header)
        for word in s:
            for c in word:
                if c in mapping:
                    sys.stdout.write(mapping[c])
                    output_file.write(mapping[c])
                elif c == '\n':
                    sys.stdout.write("")
                    output_file.write("")
                else:
                    sys.stdout.write("@")
                    output_file.write("@")
            sys.stdout.write(" ")
            output_file.write(" ")
        sys.stdout.write("\n")
        output_file.write("\n")
        case_num += 1
            
        
    output_file.close()
    
if __name__ == "__main__":
    main()