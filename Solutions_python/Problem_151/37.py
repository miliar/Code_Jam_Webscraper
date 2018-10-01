'''
Created on Apr 12, 2014

@author: ignacio
'''

import sys
import logging
import os
import collections
import itertools

if "--debug" in sys.argv:
    logging.basicConfig(level=logging.DEBUG)


def main():
    problem_input = sys.stdin
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if os.path.isfile(input_file):
            problem_input = open(input_file)
        
    cases = int(problem_input.readline())
    logging.debug(cases)
    for case in xrange(cases):
        resp = run_case(problem_input)
        print "Case #%s: %s" % (case + 1, resp,)
    
            
def run_case(problem_input):
    size, servernum = (int(x) for x in problem_input.readline().split())
    words = []
    for _x in xrange(size):
        words.append(problem_input.readline().strip())
    count = collections.defaultdict(int)
    prefixes = {word: list(_prefixes(word)) for word in words}
    
    for word_sets in _split_words(words, servernum):
        logging.debug("Wordsets: %s", word_sets)
        cost = sum(_trie_cost(ws, prefixes) for ws in word_sets)
        logging.debug("Cost: %s", cost)
        count[cost] += 1
        
    max_cost = max(count)
    return "{} {}".format(max_cost, count[max_cost])
    
    
    
def _trie_cost(word_set, prefixes):
    nodes = set()
    for word in word_set:
        for prefix in prefixes[word]:
            nodes.add(prefix)
    logging.debug("Trie for %s: %s", word_set, nodes)
    return len(nodes)
        
def _prefixes(word):
    for index in xrange(len(word) + 1):
        yield word[:index]
        
def _split_words(words, servernum):
    rwords = [[w] * servernum for w in words]
    ewords = [list(enumerate(rw)) for rw in rwords]
    for things in itertools.product(*ewords):
        dist = [[] for x in xrange(servernum)]
        for s, w in things:
            dist[s].append(w)
        if all(dist):
            yield dist

def _old_split_words(words, servernum):
    for indexes in _indexes(servernum - 1, len(words)):
        indexes = [0] + indexes + [len(words)]
        word_sets = []
        for start, end in zip(indexes, indexes[1:]):
            if start == end:
                break
            word_sets.append(words[start:end])
        else:
            yield word_sets
    
def _indexes(count, size, start=0):
    if count <= 0:
        yield []
    else:
        for x in xrange(start, size):
            for indexes in _indexes(count - 1, size, start=x + 1):
                yield [x] + indexes
            
    
   
            
if __name__ == "__main__":
    main()
