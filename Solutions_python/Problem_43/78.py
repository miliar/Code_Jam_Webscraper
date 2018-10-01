#!/usr/bin/env python

import sys
import pprint

def optimal_digit_weights():
    yield 1
    yield 0
    i = 2
    while(True):
        yield i
        i += 1

def all_your_base(phrase):
    unique = set(phrase)
    lowest_base = max(2, len(unique))
    symbol_values = {}
    weights = optimal_digit_weights()
    result = 0
    for index, symbol in enumerate(phrase):
        if not symbol in symbol_values:
            symbol_values[symbol] = weights.next()
        digit_index = (len(phrase) - 1) - index
        add = (lowest_base ** digit_index) * symbol_values[symbol]
        result += add
    return result
    

if __name__ == "__main__":
    cases = int(sys.stdin.next())
    for i in xrange(1, cases + 1):
        answer = all_your_base(sys.stdin.next().strip())
        print "Case #%d: %s" % (i, answer)
	
