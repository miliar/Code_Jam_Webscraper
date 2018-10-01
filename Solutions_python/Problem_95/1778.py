inp = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"

output = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

mapping = {}

for x, y in zip(inp, output):
    mapping[x] = y

mapping['z'] = 'q'
mapping['q'] = 'z'

t = int(input())
for i in range(t):
    print('Case #%d: %s' % (i+1, ''.join([mapping[x] for x in input()])))
