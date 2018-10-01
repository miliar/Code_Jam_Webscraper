import sys

def make_dict(googlerese, english):
    d = {}
    for i in range(len(english)):
        if googlerese[i] != ' ' and not d.has_key(googlerese[i]):
            d[googlerese[i]] = english[i]
    return d
    
googlerese_text = 'zq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
english_text = 'qz our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
googlerese2english_dict = make_dict(googlerese_text, english_text)
        
def translate_googlerese(s):
    clist = list(s)
    for i in range(len(clist)):
        if clist[i] != ' ':
            clist[i] = googlerese2english_dict[clist[i]]
    translated = ''.join(clist)
    return translated

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        f = open(filename)

    lines = f.read().splitlines()
    cases = int(lines[0])
    for i in range(1, cases + 1):
        print "Case #%i: %s" % (i, translate_googlerese(lines[i]))
