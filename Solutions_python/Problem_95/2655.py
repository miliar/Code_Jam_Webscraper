'''
Created on 14 avr. 2012

@author: jerome
'''

import sys, re

def replaceChar(character):
    if character == 'a':
        return 'y'
    elif character == 'b':
        return 'h'
    elif character == 'c':
        return 'e'
    elif character == 'd':
        return 's'
    elif character == 'e':
        return 'o'
    elif character == 'f':
        return 'c'
    elif character == 'g':
        return 'v'
    elif character == 'h':
        return 'x'
    elif character == 'i':
        return 'd'
    elif character == 'j':
        return 'u'
    elif character == 'k':
        return 'i'
    elif character == 'l':
        return 'g'
    elif character == 'm':
        return 'l'
    elif character == 'n':
        return 'b'
    elif character == 'o':
        return 'k'
    elif character == 'p':
        return 'r'
    elif character == 'q':
        return 'z'
    elif character == 'r':
        return 't'
    elif character == 's':
        return 'n'
    elif character == 't':
        return 'w'
    elif character == 'u':
        return 'j'
    elif character == 'v':
        return 'p'
    elif character == 'w':
        return 'f'
    elif character == 'x':
        return 'm'
    elif character == 'y':
        return 'a'
    elif character == 'z':
        return 'q'
    else:
        return character

def replace(chaine):
    result = ""
    for j in range(0,len(chaine)):
        result = result + replaceChar(chaine[j])
    return result

if __name__ == '__main__':
    fp = open(sys.argv[1],'r')
     
    #read params
    l = int(fp.readline())
     
    #read words
    words = [fp.readline() for x in range(l)]
    
    #read pattern
    for i in range(0, l):
        print ("Case #"+str(i+1)+": "+replace(words[i]).split("\n")[0])
    fp.close()