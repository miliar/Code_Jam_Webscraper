#!/bin/python
#Created by matekm"
import re

def makeLetters (testcase):
    """Trivial function that splits given line into single letter
       or groups of letters"""
    letters = []
    complex = False
    for i in range (len(testcase)):
        if (testcase[i] == '('):
            complex = True
            word = ""
            continue
        if (testcase[i] == ')'):
            complex = False
            letters.append (word)
            continue
        if (complex is True):
            word = word + testcase[i]
            continue
        letters.append (testcase[i])
        
    return letters, len(letters)

if __name__ == "__main__":
    # getting L, D, N from the first line of input
    first_line = raw_input ().split ()
    L, D, N = int(first_line[0]), int(first_line[1]), int(first_line[2])
    
    # reading Alien dictionary
    words = []
    for i in range (D):
        word = raw_input ()
        words.append (word)
        
    # doing testcase
    for j in range (N):
        testcase = raw_input ()
        letters, lettersLen = makeLetters (testcase)
        if (lettersLen != L):
            print "Case #{0}: {1}".format (j+1, 0)
            continue
        
        now = 0
        for word in words:
            isMatch = True
            for k in range(L):
                if word[k] not in letters[k]:
                    isMatch = False
                    break
            if (isMatch is True):
                now = now + 1
                
        print "Case #{0}: {1}".format (j+1, now)