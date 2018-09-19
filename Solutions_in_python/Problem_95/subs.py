import sys

dic = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

cnt = 0
for l in sys.stdin.readlines():
    l = l.strip()
    if cnt > 0:
        out = []
        for c in l:
            if dic.has_key( c ):
                out.append( dic[ c ] ) 
            else:
                out.append( c ) 
        print "Case #" + str( cnt ) + ": " + "".join( out )
    cnt = cnt + 1 
