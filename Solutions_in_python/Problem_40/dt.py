#!/usr/bin/python

import sys, re

class DTree:
    def __init__(self, parent = None):
        self.weight = self.feature = self.left = self.right = None
        self.state = 1
        self.parent = parent

    def __str__(self):
        if not self.weight:
            #print "WARN"
            self.weight = 0
        res = "(%f" % self.weight
        if self.feature:
            res += " " + self.feature + " "  + str(self.left) + " " + str(self.right)
        res += ")"
        return res

    @classmethod
    def parse(cls, sexp):
        #sexp.
        t = None
        word = ''
        #print sexp
        for c in sexp:
            if c == ' ' or c == '(' or c == ')':
                if word == "":
                    pass
                elif t.state == 1:
                    #print "weight: %s" % word
                    t.weight = float(word)
                    word = ""
                    t.state = 2
                elif t.state == 2:
                    t.feature = word
                    word = ""
                    t.state = 3
                else:
                    #print "HOGE" + word
                    pass

            if c == '(':
                newt = DTree(t)
                if not t:
                    t = newt
                elif t.state == 3:
                    t.left = newt
                    t.state = 4
                elif t.state == 4:
                    t.right = newt
                    t.state = 5
                t = newt
                word = ""
            elif c == ')':
                if not t.parent is None:
                    t = t.parent
                word = ""
            elif c != ' ':
                word += c
        return t

def solve_case(f):
    n = int(f.readline())
    s_exp = ""
    for i in range(0, n):
        s_exp += f.readline().strip() + " "
    tree = DTree.parse(s_exp)
    #print tree
    a = int(f.readline())
    for i in range(0,a):
        ary = f.readline().split()
        name = ary[0]
        features = ary[2:]
        #print features
        t = tree
        p = t.weight
        while t.feature:
            if t.feature in features:
                #print "left"
                t = t.left
                p *= t.weight
            else:
                #print "right"
                t = t.right
                p *= t.weight
        print "%0.7f" % p

def main():
    f = file(sys.argv[1])
    n = int(f.readline())
    for testno in range(0, n):
        print "Case #%d:" % (testno + 1)
        solve_case(f)

if __name__ == '__main__':
    main()
