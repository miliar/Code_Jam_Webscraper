cipher = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz"
plain = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq"

mapping = {}
for p, c in zip(plain, cipher):
  mapping[c] = p

print sorted(mapping.values())

#print cipher
#print plain
#print mapping

import sys
def getnum():
      return [int(x) for x in sys.stdin.readline().split()]

N, = getnum()

for n in range(1, N+1):
  p = "".join([mapping[x] for x in sys.stdin.readline()[:-1]])
  print "Case #%d: %s" % (n, p)

