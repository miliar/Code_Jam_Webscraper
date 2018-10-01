import sys

__author__ = 'joranvar'

def tr_from_sample(fr, to):
    T = int(fr.readline())
    G = ''.join(fr.readlines()) + 'y qee'
    S = ''.join([l[l.index(':') + 2:] for l in to.readlines()]) + 'a zoo'

    tr = str.maketrans(G,S)

    # We miss one letter in the examples, so deduce that translation
    missing_from = set(range(ord('a'),ord('z')+1)) - set(tr.keys())
    missing_to = set(range(ord('a'),ord('z')+1)) - set(tr.values())

    tr.update({missing_from.pop(): missing_to.pop()})

    return tr

if __name__ == "__main__":
    fi = open('a.in')
    si = open('sample.in')
    so = open('sample.out')

    tr = tr_from_sample(si,so)

    T = int(fi.readline())
    G = [l.translate(tr) for l in fi.readlines()]

    fo = open('a.out', 'w')
    fo.writelines(['Case #' + str(i) + ': ' + l for i, l in enumerate(G,1)])

