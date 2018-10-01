import sys

mapping = {
'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q',
' ': ' '
}        

def translate(line):
    f = lambda c: mapping[c]
    return ''.join(map(f, line))

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    out = open('out.txt', 'w')
    cases = int(f.readline())
    for i in xrange(1, cases + 1):
        out.write('Case #{0}: {1}\n'.format(i, translate(f.readline().replace('\n', ''))))
    f.close()
