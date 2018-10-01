#!/usr/bin/env python

import sys, re, itertools

def int_line():
    return int(sys.stdin.readline().strip())

def split_tokens(text):
    return (tkn.strip() for tkn in split_tokens.atoms.split(text) if tkn and not tkn.isspace())
split_tokens.atoms = re.compile('(\()|(\))|([a-z0-9.]+)')

def parse(text):
    return do_parse(split_tokens(text))

def parse_lines(lines):
    return do_parse(itertools.chain(*(split_tokens(ln) for ln in lines)))

def do_parse(tokens):
    result = []
    stack = [result]
    for tkn in tokens:
        if tkn == '(':
            new_list = []
            stack[-1].append(new_list)
            stack.append(new_list)
        elif tkn == ')':
            stack.pop()
        else:
            stack[-1].append(tkn)
    return transform(result[0])

def transform(tree):
    if len(tree) == 4:
        return float(tree[0]), tree[1], transform(tree[2]), transform(tree[3])
    elif len(tree) == 1:
        return float(tree[0])

no_cases = int_line()

for case in xrange(1, no_cases + 1):
    tree_len = int_line()
    tree_lines = []
    for _ in xrange(tree_len):
        line = sys.stdin.readline().strip()
        tree_lines.append(line)
    tree = parse_lines(tree_lines)
    no_animals = int_line()
    print "Case #%d:" % case
    for _ in xrange(no_animals):
        line = sys.stdin.readline().strip()
        features = set(line.split()[2:])
        node, result = tree, 1.0
        while node:
            if isinstance(node, tuple):
                weight, feat, left, right = node
                if feat in features:
                    node = left
                else:
                    node = right
            else:
                weight = node
                node = None
            result *= weight
        print '%.8f' % result
