#!/usr/bin/python2.5
# Solution to Google Code Jam 08 Round 2 Problem A
# Matt Giuca

# Usage: ./probA.py < inputfile > outputfile

import sys
import copy

DEBUG = False

class Node(object):
    """
    gate = "AND" or "OR"
    children = None or [Node]*2.
    val = 0 or 1
    changeable = bool
    """
    def __init__(self):
        self.gate = None
        self.children = None
        self.val = None
        self.changeable = False
    def addChild(self, child):
        if self.children is None:
            self.children = [child]
        else:
            self.children.append(child)

def treeFromList(nodesList):
    """
    Builds a tree from a nodes list. Mutates nodes. Returns root.
    """
    for i in range(1, len(nodesList)):
        # Add to its parent
        nodesList[(i+1)//2-1].addChild(nodesList[i])
    return nodesList[0]

def computeVals(root):
    """
    Writes 'val' for each node in the tree.
    """
    if root.gate is None:
        return

    if root.children is not None:
        computeVals(root.children[0])
        computeVals(root.children[1])

    if root.gate == "AND":
        root.val = root.children[0].val and root.children[1].val
    elif root.gate == "OR":
        root.val = root.children[0].val or root.children[1].val

def parse(file=sys.stdin):
    """
    (Generator) Read input file from filename or file or stdin,
    return a structure.
    Yields (v, a tree of Nodes (root node)).
    """
    if isinstance(file, basestring):
        file = open(file)
        toclose = True
    else:
        toclose = False
    n = int(file.readline().strip())
    for i in range(n):
        # build array of nodes
        nodes = []
        m, v = map(int, file.readline().strip().split())
        for j in range((m-1)/2):
            g, c = map(int, file.readline().strip().split())
            n = Node()
            n.gate = "AND" if g == 1 else "OR"
            n.changeable = True if c == 1 else False
            nodes.append(n)
        for j in range((m+1)/2):
            i = int(file.readline().strip())
            n = Node()
            n.val = i
            nodes.append(n)
        yield v, treeFromList(nodes)
    if toclose:
        file.close()

def min_(x, y):
    """Min, but propagate both-None as failure."""
    if x is None:
        return y
    if y is None:
        return x
    return min(x,y)

def plus_(x, y):
    """Plus, but propagate None as failure."""
    if x is None or y is None:
        return None
    else:
        return x + y

def solve_case(v, root):
    """
    Returns the cost of fixing root to v. None if impossible.
    """
    if root.val == v:
        return 0
    if root.gate is None:
        return None
    left = root.children[0].val
    right = root.children[1].val
    lr = str(left) + str(right)
    rootgate = root.gate
    cost1 = 0

    if root.changeable:
        if left ^ right:
            # Change and we're done
            return 1
        elif rootgate == "AND" and lr == "00":
            # Change and change either child to 1
            cost1 = 1
            rootgate = "OR"
        elif rootgate == "OR" and lr == "11":
            # Change and change either child to 0
            cost1 = 1
            rootgate = "AND"

    # See how many children we need to change
    if rootgate == "AND":
        if lr == "11":
            # Change either child to 0
            cost2 = min_(solve_case(0, root.children[0]),
                         solve_case(0, root.children[1]))
        else:
            # Change both children to 1
            cost2 = plus_(solve_case(1, root.children[0]),
                          solve_case(1, root.children[1]))
    else:
        if lr == "00":
            # Change either child to 1
            cost2 = min_(solve_case(1, root.children[0]),
                         solve_case(1, root.children[1]))
        else:
            # Change both children to 0
            cost2 = plus_(solve_case(0, root.children[0]),
                          solve_case(0, root.children[1]))
    if cost2 is None:
        return None
    else:
        return cost1 + cost2

def main(file=sys.stdin):
    """
    Processes input, prints output to stdout.
    """
    i = 0
    for v, root in parse(file):
        i += 1
        computeVals(root)
        answer = solve_case(v, root)
        if answer is None:
            print("Case #%d: IMPOSSIBLE" % i)
        else:
            print("Case #%d: %d" % (i, answer))

if __name__ == "__main__":
    main()
