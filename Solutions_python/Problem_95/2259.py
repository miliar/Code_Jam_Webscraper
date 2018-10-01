k = input()
for j in xrange(k):
    s = raw_input()
    r = ""
    for i in xrange(len(s)):
        if s[i] == ' ':
            r += ' '
            continue
        elif s[i] == 'y':
            r += 'a'
        elif s[i] == 'n':
            r+= 'b'
        elif s[i] == 'f':
            r+= 'c'
        elif s[i] == 'i':
            r+= 'd'
        elif s[i] == 'c':
            r+= 'e'
        elif s[i] == 'w':
            r+= 'f'
        elif s[i] == 'l':
            r+= 'g'
        elif s[i] == 'b':
            r+= 'h'
        elif s[i] == 'k':
            r+= 'i'
        elif s[i] == 'u':
            r+= 'j'
        elif s[i] == 'o':
            r+= 'k'
        elif s[i] == 'm':
            r+= 'l'
        elif s[i] == 'x':
            r+= 'm'
        elif s[i] == 's':
            r+= 'n'
        elif s[i] == 'e':
            r+= 'o'
        elif s[i] == 'v':
            r+= 'p'
        elif s[i] == 'z':
            r+= 'q'
        elif s[i] == 'p':
            r+= 'r'
        elif s[i] == 'd':
            r+= 's'
        elif s[i] == 'r':
            r+= 't'
        elif s[i] == 'j':
            r+= 'u'
        elif s[i] == 'g':
            r+= 'v'
        elif s[i] == 't':
            r+= 'w'
        elif s[i] == 'h':
            r+= 'x'
        elif s[i] == 'a':
            r+= 'y'
        elif s[i] == 'q':
            r+= 'z'
    print "Case #"+str(j+1)+": "+r