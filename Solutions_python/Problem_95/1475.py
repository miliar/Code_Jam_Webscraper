import sys

d=dict()

def train(instr, outstr):
    for i in range(len(instr)):
        d[instr[i]] = outstr[i]

train("aozq", "yeqz")
train("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
train("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
train("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")

def decode(instr):
    s = ""
    for c in instr:
        s += d[c]
    return s

numCases = int(sys.stdin.readline())
for i in range(numCases):
    print "Case #%s: %s"%(i+1, decode(sys.stdin.readline().strip("\n")))
