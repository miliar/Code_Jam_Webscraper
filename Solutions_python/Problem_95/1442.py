#!/usr/bin/python

text = ''
lines = []
mapping = {
    'a':'y', 
    'o':'e',
    'z':'q',
    'u':'j',
    'r':'p',
    'l':'m',
    'n':'s',
    'g':'l',
    'e':'c',
    'i':'k',
    's':'d',
    'm':'x',
    'p':'g',
    'b':'n',
    'd':'i',
    't':'r',
    'h':'b',
    'w':'t',
    'y':'a',
    'x':'h',
    'f':'w',
    'c':'f',
    'k':'o',
    'j':'u',
    'v':'g',
    'q':'z',
}
rmapping = {
    'y':'a', 
    'e':'o',
    'q':'z',
    'j':'u',
    'p':'r',
    'm':'l',
    's':'n',
    'l':'g',
    'c':'e',
    'k':'i',
    'd':'s',
    'x':'m',
    'g':'v',
    'n':'b',
    'i':'d',
    'r':'t',
    'b':'h',
    't':'w',
    'a':'y',
    'h':'x',
    'w':'f',
    'f':'c',
    'o':'k',
    'u':'j',
    'v':'p',
    'z':'q',
}
def translate(line):
    ret = ''
    for c in line:
        if c != ' ':
            ret += rmapping[c]
        else:
            ret += ' '
    return ret
def main():
    f=open('p1.i', 'r')
    f2=open('p1.o', 'w')
    i = 0
    for line in f:
        if i == 0:
            nt = int(line)
        else:
            tline = translate(line[:-1])
            f2.write("Case #%d: %s\n" % (i, tline))
        i += 1

if __name__ == "__main__":
    main()
