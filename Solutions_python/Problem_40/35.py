#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys

# TREE = (weight) | (weight feature TREE TREE)

def lexer(streeng):
    # All animals and features - between 1 and 10 lower case English letters.
    UNKNOWN = 1
    FLOAT = 2
    STRING = 3

    FLOAT_DIGITS = '0123456789.'
    LATIN_CHARS = 'qwertyuiopasdfghjklzxcvbnm'
    accum, mode = '', UNKNOWN
    for index, c in enumerate(streeng):
        if c in '()':
            # Flush ACCUM
            if accum:
                if mode == FLOAT:
                    yield float(accum)
                elif mode == STRING:
                    yield accum
                else:
                    assert False, 'mode should be either FLOAT or STRING'
                accum, mode = '', UNKNOWN
            # END Flush
            yield c
        elif c in FLOAT_DIGITS and mode in (FLOAT, UNKNOWN):
            mode = FLOAT
            accum += c
        elif c in LATIN_CHARS and mode in (STRING, UNKNOWN):
            mode = STRING
            accum += c
        else:
            assert c == ' ', 'Unexpected char: <%s>, str: <%s…>' % (c, streeng[index:index+20])
            # Flush ACCUM
            if accum:
                if mode == FLOAT:
                    yield float(accum)
                    accum = ''
                elif mode == STRING:
                    yield accum
                else:
                    assert False, 'mode should be either FLOAT or STRING'
                accum, mode = '', UNKNOWN
            # END Flush

# ( weight ) -> float
# ( weight feature tree tree) -> [float, string, Tree_yes, Tree_no]
def parse_subtree(lex_src, append_to):
    weight = lex_src.next()
    assert type(weight) is float
    token = lex_src.next()
    assert type(token) is str
    if token == ')':
        append_to.append(weight)
    else:
        # `token` is feature
        t_yes, t_no = [], []
        append_to.append(weight)
        append_to.append(token)
        append_to.append(t_yes)
        append_to.append(t_no)
        assert lex_src.next() == '('
        parse_subtree(lex_src, t_yes)
        assert lex_src.next() == '('
        parse_subtree(lex_src, t_no)
        assert lex_src.next() == ')'


def parse_tree(streeng):
    root = []
    lex_src = lexer(streeng)
    assert lex_src.next() == '('
    parse_subtree(lex_src, root)
    return root


N_cases = int(sys.stdin.readline())
for case in xrange(N_cases):
    L_tree_lines = int(sys.stdin.readline())
    tree = []
    for i in xrange(L_tree_lines):
        tree.append(sys.stdin.readline().strip())
    tree = ' '.join(tree)
    tree = parse_tree(tree)

    # set of features
    animals = []
    A_animal_lines = int(sys.stdin.readline())
    for i in xrange(A_animal_lines):
        animals.append(set(sys.stdin.readline().strip().split()[2:]))

    print "Case #%i:" % (case+1)
    for featureset in animals:
        p = 1.0
        root = tree
        while True:
            p *= root[0]
            assert len(root) in (1,4)
            if len(root) == 4:
                if root[1] in featureset:
                    root = root[2]
                else:
                    root = root[3]
            else:
                break
        print "%.7f" % p


# vim:set tabstop=4 softtabstop=4 shiftwidth=4 expandtab: 
