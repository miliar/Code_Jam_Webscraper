import sys

goog = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qeez"
eng = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zooq"

trans = {}
for k, letter in enumerate(goog):
    trans[letter] = eng[k]

def decode(english):
    return "".join([trans[ltr] for ltr in english])

numlines = int(sys.stdin.readline())

counter = 1
for line in sys.stdin:
    print "Case #%s:" % counter,
    print decode(line.strip())
    counter += 1

