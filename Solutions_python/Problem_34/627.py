#!/usr/bin/env python

from sys import stderr
import os, sys
from optparse import OptionParser
from datetime import datetime, timedelta
import re

class LanguageSample(object):
    
    def __init__(self):
       self.num_letters = None
       self.num_words = None
       self.num_samples = None
       
       self.word_list = []
       self.sample_list = []
        
    def _complete(self):
        
        am_complete = True
        
        if self.num_letters is None:
            am_complete = False
        elif len(self.word_list) < self.num_words:
            am_complete = False
        elif len(self.sample_list) < self.num_samples:
            am_complete = False
            
        return am_complete

    is_complete = property(_complete)
    
    def add(self, line):
        line = line.strip()
        
        if self.num_samples is None:
            self.num_letters, self.num_words, self.num_samples = [int(x) for x in line.split()]
        elif len(self.word_list) < self.num_words:
            self.word_list.append(line)
        else:
            self.sample_list.append(line)
        
    def run(self):
        
        #for each sample, build a regex and search for it 
        #in the word list
        
        case_number = 0
        
        for sample in self.sample_list:
            
            case_number += 1
            
            pattern = ''
        
            while sample:
                if sample[0] == '(':
                    closer = sample.find(')')
                    letter = "(%s)" % ('|'.join(sample[1:closer]))
                    sample = sample[closer+1:]
                else:
                    letter = sample[0]
                    sample = sample[1:]
            
                pattern += letter
                
            matches = 0
        
            for word in self.word_list:
                if re.match(pattern, word): 
                    matches += 1


            print "Case #%d: %d" % (case_number, matches)
        
                    
        

def readfile(filename):
    """
    Read and parse a file formatted
    to contain alien language words.
    """

    input = open(filename, 'r')

    instance = LanguageSample()

    for line in input:
       
        instance.add(line)
    
        if instance.is_complete:
            yield instance
            instance = LanguageSample()
            
if __name__ == '__main__':
    
    parser = OptionParser()
    
    (kwargs, args) = parser.parse_args()
    
    try:
        input_file = args[0]
    except IndexError:
        stderr.write('No input file passed.\n')
        raise ValueError, "Invalid filename passed."
        
    if not os.path.exists(input_file):
        raise ValueError, "Invalid filename passed."

    for thingy in readfile(input_file):
        thingy.run()
