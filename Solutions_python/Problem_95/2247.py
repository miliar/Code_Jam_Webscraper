import sys

gtext = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
text = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'

D = dict([(gtext[i], text[i]) for i in range(0,len(gtext))])
D['y'] = 'a'
D['e'] = 'o'
D['q'] = 'z'
D['z'] = 'q'


f = open('a.in', 'r')

num_cases = int(f.readline())

for i in range(1,num_cases+1):
    int_str = f.readline()
    out_str = "".join([D[ch] for ch in int_str if ch != '\n'])
    print 'Case #%d: %s' % (i, out_str)

f.close()


