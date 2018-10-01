import re

T = int(raw_input())

class node:
    def __init__(self, prob, feature="", left=None, right=None):
        self.p = prob
        self.f = feature
        self.l = left
        self.r = right
    
    def traverse(self, prob, features):
        prob *= self.p
        if self.isnode():
            return prob
        if self.f in features:
            return self.l.traverse(prob, features)
        return self.r.traverse(prob, features)

    def isnode(self):
        if self.l:
            return False
        return True

    def tostr(self):
        if self.isnode():
            return "( " + str(self.p) + " )"
        return "( " + str(self.p) + " " + self.f + " " + self.l.tostr() + " " + self.r.tostr() + " )"

def buildtree(s):
    #print "bt o: '"+ s+"'"
    s = s.strip()
    s = s[1:-1]
    #print "bt '"+ s+ "'"
    tokens = s.split()
    #print tokens
    if len(tokens) == 1:
        #print "single"
        #print s
        #print tokens[0]
        return node(float(tokens[0]))
    else:#has feature
        #print "feature"
        prob = float(tokens[0])
        feature = tokens[1]
        temp = ' '.join(tokens[2:])
        #print temp
        left = "(-1)"
        right = "(-1)"
        num = 0
        for i, c in enumerate(temp):
            #print "c: ", i, c, "num: ", num
            if c == '(':
                num += 1
            elif c == ')':
                num -= 1
                if num == 0:
                    left = temp[:i+1]
                    right = temp[i+2:]
                    break               
        #print 'left:' , left
        #print 'right:', right
        
        return node(prob, feature, buildtree(left), buildtree(right))
        

def solve(case):
    lines = int(raw_input())
    treestr = ""
    for i in xrange(lines):
        treestr += raw_input() + "\n"
    
    treestr = " ".join(treestr.split())
    
    tree = buildtree(treestr)
    #print "tree:", tree.tostr()

    features = []
    num = int(raw_input())
    for i in xrange(num):
        line = raw_input().split()
        temp = {}
        for feature in line[2:]:
            temp[feature] = True
        features.append(temp)
    
    print "Case #%d:"%(case)
    for i in xrange(num):
        print "%.7f"%tree.traverse(1.0, features[i])
    
for i in xrange(T):
    solve(i+1)
