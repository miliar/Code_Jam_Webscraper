from pyparsing import *
from base64 import b64decode
import pprint

def verifyLen(t):
    t = t[0]
    if t.len is not None:
        t1len = len(t[1])
        if t1len != t.len:
            raise ParseFatalException, \
                    "invalid data of length %d, expected %s" % (t1len, t.len)
    return t[1]

# define punctuation literals
LPAR, RPAR, LBRK, RBRK, LBRC, RBRC, VBAR = map(Suppress, "()[]{}|")

decimal = Word("123456789",nums).setParseAction(lambda t: int(t[0]))
bytes = Word(printables)
raw = Group(decimal.setResultsName("len") + Suppress(":") + bytes).setParseAction(verifyLen)
token = Word(alphanums + "-./_:*+=")
base64_ = Group(Optional(decimal,default=None).setResultsName("len") + VBAR 
    + OneOrMore(Word( alphanums +"+/=" )).setParseAction(lambda t: b64decode("".join(t)))
    + VBAR).setParseAction(verifyLen)
    
hexadecimal = ("#" + OneOrMore(Word(hexnums)) + "#")\
                .setParseAction(lambda t: int("".join(t[1:-1]),16))
qString = Group(Optional(decimal,default=None).setResultsName("len") + 
                        dblQuotedString.setParseAction(removeQuotes)).setParseAction(verifyLen)
simpleString = raw | token | base64_ | hexadecimal | qString

display = LBRK + simpleString + RBRK
string_ = Optional(display) + simpleString

sexp = Forward()
sexpList = Group(LPAR + ZeroOrMore(sexp) + RPAR)
sexp << ( string_ | sexpList )

file = open('A-large.in')
t = int(file.readline())
for i in range(t) :
    lines =  int(file.readline())
    s = ''.join(file.readline() for j in range(lines))
    nc = int(file.readline())
    a = [file.readline().split()[2:] for j in range(nc)]
    print "Case #%d:" % (i + 1)
    for k in a :
        tree = sexp.parseString(s)[0]
        f = 1.0
        while True :
            f *= float(tree[0])
            if len(tree) == 1 :
                break
            if tree[1] in k :
                tree = tree[2]
            else :
                tree = tree[3]

        print "%0.7f" % f
file.close()
