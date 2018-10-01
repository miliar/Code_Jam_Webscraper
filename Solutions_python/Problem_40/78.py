#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2009 Sep 12

import sys

class Node:
    def __init__(self, weight, f, left, right):
        self.weight = weight
        self.f = f
        self.left = left
        self.right = right

    def __str__(self):
        res = "(%f, %s: %s %s)" % (self.weight, self.f, self.left, self.right)
        return res


def build_tree(str):

    while (len(str) > 0) and (str[0] != '(') :
        str = str[1:]
    if len(str) == 0:
        return None, ""

    str = str[1:]
    while str[0] == ' ':
        str = str[1:]

    # get weight
    i = 0
    while (str[i] != ' ') and (str[i] != ')') and (str[i] != '('):
        i += 1
    weight = float(str[0:i])

    str = str[i+1:]

    feature = ''
    if len(str) != 0:
        # get feature if exists
        i = 0
        while (str[i] != ')') and (str[i] != '('):
            i += 1
        feature = str[0:i]

        str = str[i:]

    if len(feature) == 0:
        # node finished
        node = Node(weight, feature, None, None)
        return node, str
    else:
        # children
        left, str = build_tree(str)
        right, str = build_tree(str)
        node = Node(weight, feature, left, right)
        return node, str



def compute_cuteness(feature_list, tree):

    if tree.f in feature_list:
        if tree.left is not None:
            res = tree.weight * compute_cuteness(feature_list, tree.left)
        else:
            res = tree.weight
        return res
    else:
        if tree.right is not None:
            res = tree.weight * compute_cuteness(feature_list, tree.right)
        else:
            res = tree.weight
        return res

def main():
    file = open(sys.argv[1])

    nb_cases = int(file.readline())

    for case_nb in range(1, nb_cases + 1):

        # parse tree
        L = int(file.readline())

        t_lines = ""
        for l in range(L):
            line = file.readline().replace('\n', '')
            line.replace(' +', ' ')
            line = line.lstrip()
            t_lines += line

        tree, str = build_tree(t_lines)


        # parse animals
        A = int(file.readline())
        animals = []
        for l in range(A):
            line = file.readline().replace('\n', '')
            features = line.split(' ')[2:]
            animals.append(features)

        print "Case #%d: " % case_nb

        # compute animal cuteness
        for feature_list in animals:
            print "%.7f" % compute_cuteness(feature_list, tree)

    file.close()


if __name__ == "__main__":
    main()
