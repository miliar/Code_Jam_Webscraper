import sys
import string
T = int(sys.stdin.readline())

for caseno in xrange(T):
    line = sys.stdin.readline()
    line = line.strip()
    print "Case #%d: %s" % (caseno + 1, line.translate(string.maketrans("abcdefghijklmnopqrstuvwxyz", "yhesocvxduiglbkrztnwjpfmaq")))
