
import re, sys, pprint

# import sys
# open(sys.argv[1])

def parsetree(t):
    
    t = t.strip()
    assert t[0] == '('
    m = re.match(' *([\d.]+)( +[a-z]+)? *', t[1:])
    assert m, t[:30]
    weight = float(m.group(1))
    name = m.group(2)
    
    tail = t[m.end() + 1:]
    if name != None:
        name = name.strip()
        l1, t2 = parsetree(tail)
        l2, t3 = parsetree(t2)
        result = (weight, (name, l1, l2))
    else:
        result = (weight, None)
        t3 = tail
    m2 = re.match(' *\)', t3)
    t4 = t3[m2.end():]
    
    return result, t4

def w(tree): return tree[0]
def name(tree): return tree[1]
    
def solve_animal(tree, features, p):
    #print tree[0], p
    
    p *= tree[0] 
    sub = tree[1]
    if sub:
        if sub[0] in features:
            l = sub[1]
        else:
            l = sub[2]
        p = solve_animal(l, features, p)
    return p
            

def solvsecase(ncase):
    nlines = int(raw_input())
    tree_text = ' '.join([raw_input() for _ in range(nlines)])
    nanimals = int(raw_input())
    
    l, t = parsetree(tree_text)
    assert t.strip() == ''

    print 'Case #%d:' % ncase
    
    for _ in range(nanimals):
        animal_text = raw_input().split()
        animal_name = animal_text[0]
        animal_n_ = int(animal_text[1])
        features = animal_text[2:]
        assert len(features) == animal_n_, (features, animal_n_)
        
        #pprint.pprint(l)
        p = solve_animal(l, features, 1.0)
        
        print '%.7f' % p

ncases = int(raw_input())
for ncase in range(ncases):
    solvsecase(ncase + 1)
