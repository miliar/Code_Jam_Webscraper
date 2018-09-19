import sys
import re
from itertools import *

input = None
output = None

def readints():
    for s in islice(input, 1): 
        lst = map(int, s.split())
        return lst[0] if len(lst) == 1 else lst

tokenizerrx = re.compile(r"""\s* (
    (?P<n> \d+\.\d+ ) |
    (?P<o> \( ) | 
    (?P<c> \) ) | 
    (?P<f> [a-z]+ ) 
    ) \s* """, re.VERBOSE) 

def tokenize(s):
    pos = 0
    while pos < len(s):
        match = tokenizerrx.match(s, pos)
        if not match:
            print 'parsing failed on string: '
            print s
            print 'at pos', pos, ':', s[pos:]
            raise Exception()
        for k, v in match.groupdict().items():
            if v:
                yield (k, v)
                break
        pos = match.end()

def buildtree(tokenizer):
    assert next(tokenizer)[0] == 'o'
    p = next(tokenizer)
    assert p[0] == 'n'
    p = float(p[1])
    t = next(tokenizer)
    if t[0] == 'c':
        return p
    else:
        assert t[0] == 'f'
        trait = t[1]
        l = buildtree(tokenizer)
        r = buildtree(tokenizer)
        assert next(tokenizer)[0] == 'c'
        return (p, trait, l, r)

def walktree(tree, traits):
    p = 1.0
    if isinstance(tree, float):
        return p * tree
    else:
        p *= tree[0]
        if tree[1] in traits:
            p *= walktree(tree[2], traits)
        else:
            p *= walktree(tree[3], traits)
        return p
            
    

def solve():
    testcount = readints()
    for test in range(testcount):
        print >>output, "Case #%d:" % (test + 1)
        treelc = readints()
        tree_s = " ".join(islice(input, treelc))
        tree_t = tokenize(tree_s)
        tree = buildtree(tree_t)
        assert not list(tree_t)
        #print tree
        animalcount = readints()
        for s in islice(input, animalcount):
            ls = s.split()
            name = ls[0]
            traits = ls[2:]
            assert len(traits) == int(ls[1])
            p = walktree(tree, traits)
            print >>output, "%0.7f" % p
            

taskname = 'A'
if __name__ == '__main__':
    input = open(taskname + '-small.in', 'r')
    output = open(taskname + '-small.out', 'w')
    solve()
    print 'Small solved'
    input.close()
    output.close()

    input = open(taskname + '-large.in', 'r')
    output = open(taskname + '-large.out', 'w')
    solve()
    print 'Large solved'
    input.close()
    output.close()
      