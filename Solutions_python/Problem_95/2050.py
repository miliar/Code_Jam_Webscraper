import sys
import string

key = {
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
}

def decode(str):
    out = ''
    for j in range(0, len(str)):
        try:
            out += key[str[j]]
        except:
            out += str[j]
    return out

if __name__=="__main__":
    fp = open(sys.argv[1])

    inputs = int(fp.readline())

    for j in range(1,inputs+1):
        print "Case #%s: %s" % (j, decode(fp.readline()).strip())

    fp.close()

