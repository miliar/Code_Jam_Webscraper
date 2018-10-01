source = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv aozq"
dest = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up yeqz"

trans = {}

for i in range(len(source)):
    if source[i] not in trans:
        trans[source[i]] = dest[i]

f = open("trans.in", 'r')
cases = 1
case = 0
for line in f.readlines():
    if case > cases:
        break
    if case != 0:
        val = "Case #" + str(case) + ": "
        for i in range(len(line)-1):
            val = val + trans[line[i]]
        print val
    else:
        cases = int(line)
    case = case + 1
