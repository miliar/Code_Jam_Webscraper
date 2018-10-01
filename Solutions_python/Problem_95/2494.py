#!/usr/bin/env python
import sys
import string

inmap="abcdefghijklmnopqrstuvwxyz"
otmap="yhesocvxduiglbkrztnwjpfmaq"
goog_map = string.maketrans(inmap, otmap)
def googlese_map(instring):

     
    return instring.translate(goog_map)

def main():
    """point of code entry"""
    #read test input from stdin, write results to stdout
    num_cases = int(sys.stdin.readline().rstrip('\n'))
    for idx in xrange(1, num_cases + 1):
        inline = sys.stdin.readline().rstrip('\n')
        outline = "Case #%d: %s\n" % (idx, googlese_map(inline))
        sys.stdout.write(outline)

if __name__ == '__main__':
    main()
