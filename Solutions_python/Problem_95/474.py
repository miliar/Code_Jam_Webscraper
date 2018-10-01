import sys

mapping = \
{' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q'}

def solve(str):
    return ''.join(mapping[c] for c in str)

def main():
    with open(sys.argv[1]) as f:
        f.readline()
        for i, line in enumerate(f):
            res = solve(line.strip())
            print 'Case #%d: %s' % (i+1, res)

if __name__ == "__main__":
    main()
