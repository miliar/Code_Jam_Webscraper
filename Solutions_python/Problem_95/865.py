#!/usr/bin/env python
import sys

m = {
    ' ': ' ',
    'y': 'a',
    'e': 'o',
    'q': 'z',
    'j': 'u',
    'r': 't',
    'b': 'h',
    'c': 'e',
    'p': 'r',
    'y': 'a',
    't': 'w',
    's': 'n',
    'a': 'y',
    'd': 's',
    'k': 'i',
    'h': 'x',
    'w': 'f',
    'f': 'c',
    'e': 'o',
    'm': 'l',
    'v': 'p',
    'n': 'b',
    'o': 'k',
    'j': 'u',
    'u': 'j',
    'l': 'g',
    'g': 'v',
    'x': 'm',
    'i': 'd',
    'z': 'q', #only char that is not mapped
}

def main():
    i = sys.stdin
    o = sys.stdout

    count = int(i.readline().strip())

    caseno = 1
    for line in i:
        if caseno > count:
            break

        o.write("Case #{0}: ".format(caseno))

        for ch in line.strip():
            if ch in m:
                o.write(m[ch])
            else:
                o.write("?")

        o.write("\n")
        caseno = caseno + 1


if __name__ == '__main__':
    main()