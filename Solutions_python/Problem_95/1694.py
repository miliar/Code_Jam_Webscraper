lang1 = u'''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
lang2 = u'''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

mapping = {ord(a):b for a,b in zip(lang1, lang2)}
mapping.update({ord(u'q'): u'z', ord(u'z'): u'q'})

import sys
it = iter(sys.stdin)
next(it)
for i, line in enumerate(it, 1):
    print u'Case #{}: {}'.format(i, unicode(line.strip()).translate(mapping))
