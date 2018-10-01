import sys
import string
fi = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')
fr = fi.readline
T = int(fr())

trans = string.maketrans("abcdefghijklmnopqrstuvwxyz", \
        "yhesocvxduiglbkrztnwjpfmaq")

for t in xrange(T):
    fo.write("Case #%d: %s\n" % (t+1, fr().strip().translate(trans)))

fo.close()
