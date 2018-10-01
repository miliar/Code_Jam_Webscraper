f = open('A-small-attempt0.in')
oo = open('A1.out','w')
trans = {' ':' ','\n':'\n','a':'y', 'c':'e', 'b':'h', 'e':'o', 'd':'s', 'g':'v', 'f':'c', 'i':'d', 'h':'x', 'k':'i',\
         'j':'u', 'm':'l', 'l':'g', 'o':'k', 'n':'b', 'p':'r', 's':'n', 'r':'t', 'u':'j', 't':'w', 'w':'f', 'v':'p', 'y':'a', 'x':'m','q':'z','z':'q'}
T = int(f.readline())
for cas in range(T):
    s1 = f.readline()
    s2 = ""
    L = len(s1)
    for p in range(L-1):
        s2 = s2+trans[s1[p]]
    print "Case #"+str(cas+1)+": "+s2
