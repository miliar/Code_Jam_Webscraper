#!python

import sys
import re

class BTree:
    left = None
    right = None
    weight = 0.0
    tag = ""
    def __init__(self, weight, tag=""):
        self.weight = weight
        self.tag = tag

    def print_tree(self):
        if self.tag == "":
            print "%.3f" % (self.weight)
        else:
            print "%.3f\t%s" % (self.weight, self.tag)
            self.left.print_tree()
            self.right.print_tree()
        

if len(sys.argv) != 2:
    print "Supply a filename."
    exit(-1)

fn = sys.argv[1]

fh = open(fn, 'r')

text = fh.read().split('\n')

n = int(text[0])
text = text[1:]

def make_btree(full_tree):
    matches = re.match("^\s*\(\s*([0-9\.]+)\s*(\w*)\s*(.*)\)\s*$", full_tree)
    if matches is None:
        print "NO MATCHES FOUND! %s" % full_tree
        return BTree(0.0)
    weight = float(matches.group(1))
    tag = ""
    if len(matches.groups()) >= 2:
        tag = matches.group(2)
    next = BTree(weight, tag)
    if tag != "":
        remainder = matches.group(3)
        parens = 1
        if remainder[0] != '(':
            print "MALFORMED SUBTREE! %s" % (remainder)
            exit(1)

        c = 1
        while parens > 0:
            if remainder[c] == '(':
                parens += 1
            elif remainder[c] == ')':
                parens -= 1
            c += 1
        left = remainder[0:c]
        right = remainder[c:]
        next.left = make_btree(left)
        next.right = make_btree(right)

    return next

def find_cuteness(attr_dict, tree, prob):
    if tree.tag == "":
        return prob * tree.weight
    elif attr_dict.setdefault(tree.tag, 0):
        return find_cuteness(attr_dict, tree.left, prob*tree.weight)
    return find_cuteness(attr_dict, tree.right, prob*tree.weight)

for i in xrange(0, n):
    n_lines = int(text[0])
    text = text[1:]
    full_tree = ""

    for j in xrange(0, n_lines):
        full_tree += text[j]

    tree = make_btree(full_tree)
  
    text = text[n_lines:]
    n_animals = int(text[0])
    text = text[1:]
    print "Case #%d:" % (i+1)
    for j in xrange(0, n_animals):
        animal = text[j]
        fields = animal.split()
        name = fields[0]
        num_attrs = int(fields[1])
        fields = fields[2:]
        attr_dict = {}
        for attr in fields:
            attr_dict[attr] = 1

        print "%.7f" % (find_cuteness(attr_dict, tree, 1))

    text = text[n_animals:]


fh.close()
