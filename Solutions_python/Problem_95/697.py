# Python 2.7

reverse = {}

reverse['y'] = 'a'
reverse['o'] = 'e'
reverse['z'] = 'q'


ciphr = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv".replace(' ', '')
clear = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up".replace(' ', '')
alph = map(chr, range(ord('a'), ord('z')+1))

for a,b in zip(ciphr, clear):
  reverse[a] = b

missing_keys = sorted(set(alph).difference(set(reverse.keys())))
free_values = sorted(set(alph).difference(set(reverse.values())))

if 1 is len(missing_keys) is len(free_values): # which it is
  reverse[missing_keys[0]] = free_values[0]
else:
  raise ValueError("INSUFFICIENT DATA FOR MEANINGFUL ANSWER.")

#print reverse
t = int(raw_input())

for i in range(t):
  g = raw_input()
  print "Case #%d: %s" % (i+1, "".join(map(lambda x:reverse[x] if x != ' ' else ' ', g)))

