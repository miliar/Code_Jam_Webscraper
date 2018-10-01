#!/usr/bin/env python 
################################################################################

import sys
import os
import logging

from mpmath import *
mp.dps = 300

#if (os.environ.get("DEBUG") != None):
#logging.basicConfig(level=logging.DEBUG)

def tokenize_tree(decision_tree):
    decision_tree = decision_tree.replace("(", " ( ")
    decision_tree = decision_tree.replace(")", " ) ")
    decision_tree = decision_tree.replace("\n", " ")
    return decision_tree.split()

class Tree:
    def __init__(self, weight, feature=None, left=None, right=None):
        self.weight = mpf(weight)
        self.feature = feature
        self.left = left
        self.right = right

    def __str__(self):
        return self.str_rec("")

    def str_node(self):
        return "(weight=" + str(self.weight) +" feature=" + str(self.feature) + ")"

    def str_rec(self, tab):
        ret = tab + "(weight=" + str(self.weight)
        if (self.feature != None):
            ret += " feature=" + str(self.feature)
        if (self.left != None):
            ret += "\n" + self.left.str_rec(tab + "  ")
        if (self.right != None):
            ret += "\n" + self.right.str_rec(tab + "  ")
        ret += "\n" + tab + ")"
        #ret = ["(", weight, feature, left, right, ")"]
        return ret

def parse_tree(input):
    #print input
    assert input.pop(0) == "("

    weight = input.pop(0)

    if (input[0] == ")"):
        input.pop(0)
        return Tree(weight)
    else:
        feature = input.pop(0)
        left = parse_tree(input)
        right = parse_tree(input)
        assert input.pop(0) == ")"
        return Tree(weight, feature, left, right)

    return None



def main():
    input = sys.stdin
    
    N = int(input.readline())
    logging.info("N = %d", N)
    
    for i in range(N):
        # lines in decision tree
        L = int(input.readline())
        decision_tree = ""
        for j in range(L):
            decision_tree += input.readline()

        decision_tree = parse_tree(tokenize_tree(decision_tree))

        # number of animals
        A = int(input.readline())
        animals = []
        for j in range(A):
            line = input.readline().split()
            animals.append((line[0], line[2:]))
        processTestCase(i + 1, decision_tree, animals)


def traverseTree(tree, features):
    #print "traverseTree ", tree.str_node()

    if (tree.feature == None):
        return tree.weight
    
    if (tree.feature in features):
        return tree.weight * traverseTree(tree.left, features)
    else:
        return tree.weight * traverseTree(tree.right, features)


def processTestCase(index, decision_tree, animals):
    logging.info("index=%d,\ndecision_tree=\n%s,\nanimals=%s", index, decision_tree, animals)

    prob = 1.0

    print "Case #" + str(index) + ":"

    for (animal, features) in animals:
        #print animal, features
        features = set(features)
        prob = mpf(1.0) * traverseTree(decision_tree, features)
        #nprint(prob, 12)
        prob = float(prob)
        print "%0.12f" % prob
        #print "%0.20f" % prob
        

    
main()
sys.exit(0)
