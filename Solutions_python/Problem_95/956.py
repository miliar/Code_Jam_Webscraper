f = open('google_01_input','r')
nr = int(f.readline())

caesar = {' ': 0, 'a': -24, 'c': -2, 'b': -6, 'e': -10, 'd': -15, 'g': -15, 'f': 3, 'i': 5, 'h': -16, 'k': 2, 'j': -11, 'm': 1, 'l': 5, 'o': 4, 'n': 12, 'q': -9, 'p': -2, 's': 5, 'r': -2, 'u': 11, 't': -3, 'w': 17, 'v': 6, 'y': 24, 'x': 11, 'z': 9}

for a in xrange(0,nr):
    msg = 'Case #'+str(a+1)+': '
    for c in f.readline():
        try: msg+=chr(ord(c)-caesar[c])
        except: pass
    print msg