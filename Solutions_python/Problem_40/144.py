#!/usr/bin/env python
#coding=utf-8

problem = 'aa'
input_file_name = problem + ".in"
output_file_name = problem + ".out"
test_data = """2
3
(0.5 cool
  ( 1.000)
  (0.5 ))
2
anteater 1 cool
cockroach 0
13
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
3
beaver 2 furry freshwater
trout 4 fast freshwater fishy rainbowy
dodo 1 extinct
"""
test_data = None


class NODE(object):
    def __init__(self, p, f):
        self.p = p
        self.f = f
        self.first = None
        self.second = None
    
    def go(self, fset, p):
#        print self.p, self.f
        p *= self.p
        if '' == self.f:
            return p
        else:
            if self.f in fset:
                return self.first.go(fset, p)
            else:
                return self.second.go(fset, p)


def gen_tree(raw):
    assert(raw[0] == '(')
    assert(raw[-1] == ')')
    
    tmp = raw[1:-1].strip()
    pos = tmp.find('(')
    if -1 == pos:
        #leaf
        node = NODE(float(tmp), "")
        return node
    
    pos2 = tmp.find(' ')
    p = float(tmp[:pos2])
    f = tmp[pos2:pos].strip()
    node = NODE(p, f)
    nest = 0
    pos2 = -1
    for i in range(pos, len(tmp)):
        if '(' == tmp[i]:
            nest += 1
        elif ')' == tmp[i]:
            nest -= 1
        if 0 == nest:
            pos2 = i+1
            break
    node.first = gen_tree(tmp[pos:pos2])
    node.second = gen_tree(tmp[tmp.find('(', pos2):])
    return node

def process(input):
    output = []
    iLine = 0
    N = int(input[iLine].strip())
    iLine += 1
    for case in range(1, N + 1):
        print "Case %d"%case
        
        ##########################
        # Get source data here
        L = int(input[iLine].strip())
        iLine += 1
        raw_tree = ""
        for i in range(L):
            raw_tree += input[iLine].strip()
            iLine += 1
        raw_tree = raw_tree.strip()
#        print raw_tree
        root = gen_tree(raw_tree)
        A = int(input[iLine].strip())
        iLine += 1
        aa = list()
        for i in range(A):
            aaline = input[iLine].strip()
            iLine += 1
            aaf = aaline.split()
            tset = set()
            k = int(aaf[1])
            for j in range(k):
                tset.add(aaf[j+2])
            aa.append(tset)
#        for _k in aa:
#            print _k
        

        ##########################
        # Solve the case here
        output.append(case)
        output.append(A)
        for a in aa:
            result = root.go(a, 1)
            output.append(result)
        ##########################
        
        
    return output

def main():
    input = None
    if test_data is None:
        ifile = open(input_file_name)
        input = ifile.readlines()
        ifile.close()
    else:
        input = test_data.split('\n')
        
    output = process(input)
    
    if test_data is None:
        ofile = open(output_file_name, 'w')
        ii = 0
        while ii < len(output):
            print >> ofile, "Case #%d:"%(output[ii])
            ii += 1
            nn = output[ii]
            ii += 1
            for jj in range(nn):
                print >> ofile, "%.7f"%output[ii]
                ii += 1        
        ofile.close()
        
    ii = 0
    while ii < len(output):
        print "Case #%d:"%(output[ii])
        ii += 1
        nn = output[ii]
        ii += 1
        for jj in range(nn):
            print "%.7f"%output[ii]
            ii += 1
            
        
    return len(output)
        
if __name__ == "__main__":
    import time
    start = time.time()
    N = main()
    print "Done in %f seconds"%(time.time() - start)
    print "Average %f milliseconds"%((time.time() - start) * 1000 / N)
    
