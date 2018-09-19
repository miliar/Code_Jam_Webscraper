google = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
english = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
google = ''.join(google.split())
english = ''.join(english.split())
trans = {}
for i in xrange(len(google)):
    trans[google[i]] = english[i]
trans['q'] = 'z'
trans['z'] = 'q'

f = open('input.txt', 'r')
out = open('output.txt', 'w')
n = int(f.readline().strip())
for i in xrange(n):
    line = f.readline()
    s = 'Case #%s: ' % str(i+1)
    for c in line:
        if c in trans:
            s += trans[c]
        else:
            s += c
    out.write(s.strip() + "\n")
out.close()
        
    
