'''
Created on Apr 13, 2012

@author: aaron
'''
import sys

def getOutput(line):
    return line.split(' ', 2)[2];

if __name__ == '__main__':
    infile = open("insample.txt")
    outfile = open("outsample.txt")
    #from hint
    mappings = {'y':'a', 'e':'o', 'q':'z'}
    inLines = infile.readlines()
    outlines = outfile.readlines()
    if int(inLines[0]) != len(inLines) - 1:
        print("Invalid number of inputs.", file=sys.stderr)
        exit(1)
    for i, line in enumerate(inLines[1:]):
        print(line, end='')
        outline = getOutput(outlines[i])
        print(outline)
        for i, char in enumerate(line):
            if char not in mappings:
                mappings[char] = outline[i]
            elif mappings[char] != outline[i]:
                print("error on", char)
    
    #print out results and determine missing mapping
    a = ord('a')
    unusedChars = list(chr(a + i) for i in range(26))
    for i in range(26):
        char = chr(a + i)
        if(char in mappings):
            unusedChars.remove(mappings[char])
            print(char, mappings[char])
        else:
            missingChar = char
            print(char, "not in mappings")
    mappings[missingChar] = unusedChars[0]
    print(mappings)
    
