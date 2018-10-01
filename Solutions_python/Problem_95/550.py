#!/usr/bin/env python

base = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"

result = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

mapping = {}

for key,val in zip(base, result):
  mapping[key] = val

mapping['q'] = 'z' 
mapping['z'] = 'q' 

#print sorted(mapping.keys())
#print sorted(mapping.values())

num_of_cases = int(raw_input())

num = 1

while num <= num_of_cases:
  case = raw_input()
  print "Case #" + str(num) + ": " + reduce(lambda x,y:x+y,map(lambda x:mapping[x], case))
  num += 1
