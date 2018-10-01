'''
Created on Apr 14, 2012

@author: silent
'''

import sys
import string

googlerese_alphabet = "ynficwlbkuomxsevzpdrjgthaq"
googlerese_dic = {}

for idx in range(26):
    googlerese_dic[googlerese_alphabet[idx]] = string.ascii_lowercase[idx]
googlerese_dic[' '] = ' ' 

def get_input(input_file):
    infile = open(input_file)
    return infile

def get_output(output_file):
    outfile = open(output_file, "w")
    return outfile

def translate(googlerese_text):
    result = ""
    for idx in range(len(googlerese_text)):
        result += googlerese_dic[googlerese_text[idx]]
    return result

if __name__ == '__main__':
    if len(sys.argv) == 1:
        input_file = 'input.in'
    else:
        input_file = sys.argv[1]
    filename = input_file.split(".")[0]
    infile = get_input(input_file)
    outfile = get_output(filename + ".out")
    
    t = int(infile.readline())
    
    for case_num in range(t):
        googlerese_text = infile.readline().rstrip()
        result = translate(googlerese_text)
        
        outfile.write("Case #%d: %s\n" % (case_num+1, result))
    
    infile.close()
    outfile.close()
