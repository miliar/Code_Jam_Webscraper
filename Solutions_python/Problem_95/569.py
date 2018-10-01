d = {' ': ' ',
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
 'q': 'z',
 'o': 'k',
 'p': 'r',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q',
 '\n': '\n'}

# Just to found the characters mapping
def encode(s1, s2, d):  
    for i in xrange(len(s1)):
        d[s1[i]] = s2[i]
    return d
    
def decode(s1, d):
    s = ''
    for i in xrange(len(s1)):
        s += d[s1[i]]
    return s

def load(filename):
    l = open(filename).readlines()
    l = l[1:]
    
    return l
    
def solve(filename, outputfilename, d):
    l = load(filename)
    f = open(outputfilename, "w")
    
    for n,line in enumerate(l):
        f.write("Case #" +  str(n+1) + ": " + decode(line, d))
    
    f.close()
        
