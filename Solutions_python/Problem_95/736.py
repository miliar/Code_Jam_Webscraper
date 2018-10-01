"""
Code jam qualification question 1 
"""

import sys
import string
from collections import defaultdict

def load_tests(path):
    f = file(path)
    num_tests = int(f.readline())
    tests = f.readlines()
    assert num_tests == len(tests)
    return tests

def translate(mapping, sentence, n):
    
    ret = []
    for word in sentence.lower().split():
        trans_word = ''
        for i in xrange(len(word) + 1 - n):
            trans_word += mapping[word[i : i + n].lower()][0]
        
        ret.append(trans_word)
        
    return ' '.join(ret)

def main():
    tests = load_tests(sys.argv[1])
    
    mapping = {}
    mapping.update({'y' : 'a', 
                    'e' : 'o', 
                    'q' : 'z',
                    'j' : 'u',
                    'p' : 'r',
                    'm' : 'l',
                    's' : 'n',
                    'l' : 'g',
                    'k' : 'i',
                    'c' : 'e',
                    'd' : 's',
                    'x' : 'm',
                    'v' : 'p',
                    'm' : 'l',
                    'n' : 'b',
                    'r' : 't',
                    'i' : 'd',
                    'b' : 'h',
                    't' : 'w',
                    'a' : 'y',
                    'h' : 'x',
                    'w' : 'f',
                    'f' : 'c',
                    'o' : 'k',
                    'u' : 'j',
                    'g' : 'v',
                    'z' : 'q'})
    
    test_num = 1
    for test in tests:
        print 'Case #%d:' % test_num, translate(mapping, test, 1)
        test_num += 1
        
if '__main__' == __name__:
    main()