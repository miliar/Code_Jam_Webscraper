#!/usr/bin/python

import sys

filename = sys.argv[1]

class node:
    def __init__(self, alphabetLength):
        self.alphabetLength = alphabetLength 
        self.content = []
        for x in range(alphabetLength):
            self.content.append([False])
        self.found = 0
    def reset_found(self):
        self.found = 0
        print "something resetted"
    def add(self, word):
        index = ord(word[0]) - ord('a')
        # if the child doesn't already exist, add one
        if not self.content[index][0]:
            self.content[index][0] = True
            # you're gonna add a proper child or
            # a label "endOfWorld"
            if len(word[1:]) > 0:
                child = node(self.alphabetLength)
                self.content[index].append(child)
            else:
                self.content[index].append("endOfWord")
        if len(word[1:]) > 0:
            # call add method on the child recursively
            self.content[index][1].add(word[1:])
    def lookup(self, word):
        index = ord(word[0]) - ord('a')
        if self.content[index][0]:
            if self.content[index][1] == "endOfWord":
                return 1
            else:
                return self.content[index][1].lookup(word[1:])
        else:
            return 0
    def lookup_pattern(self, pattern):
        cp = pattern[0]
        for l in cp:
            index = ord(l) - ord('a')
            if self.content[index][0] and self.content[index][1] != "endOfWord":
                self.content[index][1].lookup_pattern(pattern[1:])
            if self.content[index][0] and self.content[index][1] == "endOfWord":
                self.found = self.found + 1
        return
    def retrieve(self):
        for i in range(self.alphabetLength):
            if self.content[i][0] and self.content[i][1] != "endOfWord":
                self.found = self.found + self.content[i][1].retrieve()
            if self.content[i][0] and self.content[i][1] == "endOfWord":
                return self.found
        return self.found
    def clean(self):
        for i in range(self.alphabetLength):
            if self.content[i][0] and self.content[i][1] != "endOfWord":
                self.content[i][1].clean()
            if self.content[i][0] and self.content[i][1] == "endOfWord":
                self.reset_found()

def tokenizePattern(Pattern):
    tPattern = []
    i = 0
    while i < len(Pattern):
        if Pattern[i] != '(':
            tPattern.append(Pattern[i])
            i = i + 1
        else:
            i = i + 1
            temp = ''
            while Pattern[i] != ')':
                temp = temp + Pattern[i]
                i = i + 1
            tPattern.append(temp)
            i = i + 1
    return tPattern

def countOccurrences(pattern, trie):
    tPattern = tokenizePattern(pattern)
    occ = []
    trie.lookup_pattern(tPattern)
    print "I retrieve and clean"
    occ = trie.retrieve()
    return occ;

inputFile = open(filename, 'r')
LDN = inputFile.readline()
LDNList = LDN.split()
Letters = int(LDNList[0])
DictLen = int(LDNList[1])
NTrials = int(LDNList[2])

Dict = []

for i in range(DictLen):
    line = inputFile.readline()
    Dict.append(line.rstrip('\n'))


Patterns = []

for i in range(NTrials):
    line = inputFile.readline()
    Patterns.append(line.rstrip('\n'))

inputFile.close()

occCount = []

print str(Letters) + " letters"
print str(DictLen) + " words"
print str(NTrials) + " patterns"
print str(len(Patterns)) + " patterns stored"

for i in range(len(Patterns)):
    myTrie2 = node(26)
    for j in range(DictLen):
        myTrie2.add(Dict[j])
    occ = countOccurrences(Patterns[i], myTrie2)
    print "pattern " + str(i) + ": " + str(occ) + " occurences"
    occCount.append(occ)


# occCount = map((lambda pattern: countOccurrences(pattern, myTrie2)), Patterns)

outputFile = open('output.txt', 'w')

for i in range(NTrials):
    outputFile.write('Case #' + str(i+1) + ': ' + str(occCount[i]) + '\n')

outputFile.close()

