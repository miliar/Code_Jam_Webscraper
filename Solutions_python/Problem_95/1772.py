a="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up aozq"
b="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv yeqz"
alphabet="abcdefghijklmnopqrstuvwxyz"
mapp={}
for i in xrange(len(a)):
  if b[i] not in mapp:
    mapp[b[i]]=a[i]
cases = int(raw_input())
for c in xrange(cases):
  print "Case #"+str(c+1)+":","".join(map(lambda x: mapp[x], raw_input()))
