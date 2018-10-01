class Node:
    def __init__(self, weight, feature):
        self.weight = weight
        self.feature = feature
        self.left = self.right = None

    def eval(self, feats):
        p = self.weight
        if self.feature in feats:
            p *= self.left.eval(feats)
        else:
            p *= self.right.eval(feats)
        return p

class Leaf:
    def __init__(self, weight):
        self.weight = weight

    def eval(self, feats):
        return self.weight

def parse_float(s, i, l):
    f = ''
    while (i < l) and (s[i] in '.0123456789'):
        f += s[i]
        i += 1
    return float(f), i

def parse_string(s, i, l):
    f = ''
    while (i < l) and (s[i] in 'abcdefghijklmnopqrstuvwxyz'):
        f += s[i]
        i += 1
    return f, i

def parse(s, i, l):
    while (i < l) and (s[i] != ')'):
        if s[i] == '(':
            i += 1
            w, i = parse_float(s, i, l)
            if s[i] == ')':
                return Leaf(w), (i + 1)
            else:
                f, i = parse_string(s, i, l)
                n = Node(w, f)
                n.left, i = parse(s, i, l)
                n.right, i = parse(s, i, l)
                return n, (i + 1)

def parse_tree(lines):
    s = ''.join(lines).replace(' ', '')
    n, i = parse(s, 0, len(s))
    return n

N = int(raw_input())
for i in xrange(1, N + 1):
    L = int(raw_input())
    lines = [raw_input() for n in xrange(L)]
    tree = parse_tree(lines)
    A = int(raw_input())
    print 'Case #%d:' % i
    for j in xrange(A):
        l = raw_input()
        feats = l.split()[2:]
        feats = set(feats)
        print '%06f' % tree.eval(feats)
