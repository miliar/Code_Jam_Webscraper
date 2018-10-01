__author__ = 'khayong'

import sys

dict = {}
list_char = []
fi = None
fo = None

def init_dict(g, s):
    g = list(g)
    s = list(s)
    for i in range(0, len(g)):
        if g[i] != ' ':
            dict[g[i]] = s[i]

def convert(g):
    str = ''
    g = list(g)
    for c in g:
        if c == ' ':
            str += c
        else:
            str += list_char[ord(c) - 97]

    return str

def main():
    init_dict("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
    init_dict("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
    init_dict("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
    init_dict("y", "a")
    init_dict("e", "o")
    init_dict("q", "z")
    init_dict("z", "q")

    for key in sorted(dict.keys()):
        list_char.append(dict[key])

    fi = file(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")
    T = int(fi.readline().strip())
    for t in range(1, T + 1):
        fo.writelines("Case #%d: %s\n" % (t, convert(fi.readline().strip())))

    


if __name__ == "__main__":
    main()