#!/usr/bin/env python
import sys

class NameN(object):
    def __init__(self, name, n):
        self.name = name
        self.n = int(n)
        self.substrings = self.get_substrings()
        self.match_count = self.get_match_count()

    def get_match_count(self):
        count = 0
        for element in self.substrings:
            if self.consonant_groups(element, self.n):
                count += 1
        return count

    def consonant_groups(self, string, n):
        current_run = 0
        #print "\n\n",string
        if len(string) < n:
            return False

        for letter in string:
            #print "looking at {letter} of {string}".format(letter=letter, string=string)
            if letter not in ['a', 'e', 'i', 'o', 'u']:
                #print "letter is NOT a vowel"
                current_run += 1
            else:
                #print "letter is a vowel"
                current_run = 0

            #print "current run: %d, target: %d" % (current_run, n)
            if current_run == n:
                #print "return True"
                return True
        return False

    def get_substrings(self):
        substrings = []
        for i in range(len(self.name)):
            for j in range(len(self.name)):
                if j == 0:
                    substrings.append(self.name[i:])
                elif j >= i:
                    substrings.append(self.name[i:j])

        return substrings

try:
    source_file = open(sys.argv[1], 'r')
except:
    print 'Error opening file'
    sys.exit(0)

line = source_file.readline()
total_cases = int(line)

# read file
cases = []

while 1:
    line = source_file.readline()
    if not line:
        break

    this_set = line
    (name, n) = line.split()
    #print name, n
    cases.append(NameN(name, n))

#print "total cases: %s" % total_cases
#print "number found: %s" % len(cases)

i = 1;
for case in cases:
    print "Case #%s: %s" % (i, case.match_count)
    i += 1

