'''
Created on Apr 13, 2012

@author: Samuel
'''
from string import maketrans

trans = maketrans("abcdefghijklmnoprstuvwxyqz", "yhesocvxduiglbkrtnwjpfmazq")

f = None
try:
    f = open("A-small-attempt1.in")
except IOError:
    pass
N = int(f.readline())
for i in range(N):
    print "Case #%d: %s" % (i+1, f.readline().translate(trans)),
    