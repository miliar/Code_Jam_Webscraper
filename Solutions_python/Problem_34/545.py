from __future__ import with_statement
import sys
import re

class AlienLanguage:
  
    def __init__(self, lowercase):
        self.words = []
        self.lowercase = int(lowercase)
        
    def addWord(self, word):
        self.words.append(word)
      
    def possibilities(self, test):
        exp = toRegExp(test)
        p = 0
        for word in self.words:
            if re.match(exp, word) != None and\
              len(word.translate(None, "QWFPGJLUYARSTDHNEIOZXCVBKM")) == self.lowercase:
                p += 1
        return p
    
    
def toRegExp(word):
    regexp = ""
    inGroup = False
    for i in range(len(word)):
        if word[i] == "(":
            inGroup = True
            regexp += "["
        elif word[i] == ")" and inGroup:
            inGroup = False
            regexp = regexp[0:-1] + "]"
        elif inGroup:
            regexp += word[i] + "|"
        else:
            regexp += word[i]
    return regexp
     
w = open(sys.argv[1].replace("in", "out"), 'w')

with open(sys.argv[1]) as f:
    words = False
    i = 1
    j = 1
    for line in f:
        if not words:
            vals = line.split()
            words = int(vals[1])
            lang = AlienLanguage(vals[0])
        elif j <= words:
            lang.addWord(line.strip())
            j += 1
        else:
            w.write("Case #%s: %s\n" % (i, lang.possibilities(line.strip())))
            i += 1
