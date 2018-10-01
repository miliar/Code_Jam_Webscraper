# Copyright (c) 2011 Jann Kleen jann@pocketvillage.com
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# from https://github.com/JannKleen/CodeJamHelper
from codejamio import *
from codejamhelper import *


from itertools import izip

# helpers
def zip_chunkwise(t, size=2):
    it = iter(t)
    return izip(*[it]*size)
    
def transposed(lists):
    if not lists: return []
    return map(lambda *row: list(row), *lists)
    
def turn_90_cw(lists):
    lists = transposed(lists)
    for li in lists:
        li.reverse()
    return lists
    
def turn_90_ccw(lists):
    lists = transposet(lists)
    lists.reverse()
    return lists
    
# data types
list_of_ints = lambda x: map(int, x.split())

def merger(rule, elements):
    if elements == []: return []
    before = elements
    after = elements.replace(rule[:2], rule[2]).replace(rule[1]+rule[0], rule[2])
    if before == after: return None
    return after
        
def shizzler(rule, elements):
    if elements == []: return []
    if rule[0] == elements[-1] and rule[1] in elements:
        return ""
    if rule[1] == elements[-1] and rule[0] in elements:
        return ""
    return elements
        
cases = CodeJamHelper(get_file()).getInputList()
for case in cases:
    case = case.split()
    mergers = []
    shizzlers = []
    for idx in xrange(0, int(case.pop(0))):
        mergers.append(case.pop(0))
    for idx in xrange(0, int(case.pop(0))):
        shizzlers.append(case.pop(0))
    #print mergers
    #print shizzlers
    case.pop(0)
    string = case.pop(0)
    print "input: %s" % string
    idx = 1
    while idx < len(string):
        for rule in mergers:
            if merger(rule, string[idx-1:idx+1]):
                print "merge %s + %s + %s" % (string[:idx-1], merger(rule, string[idx-1:idx+1]), string[idx+1:])
                string = string[:idx-1] + merger(rule, string[idx-1:idx+1]) + string[idx+1:]
                idx -= 1
                break
        for shizzle in shizzlers:
            reset = False
            if shizzler(shizzle, string[:idx+1]) == "":
                print "shizzle to %s" % shizzler(shizzle, string[:idx+1]) + string[idx+1:]
                reset = True
            string = shizzler(shizzle, string[:idx+1]) + string[idx+1:]
            if reset:
                idx = 0
        idx += 1
    print string
    
    
results = ['a']
put_file(results)