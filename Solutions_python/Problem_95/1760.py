#!/usr/bin/python
from sys import *

# build mapping
input = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv yeq"

output = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up aoz"

dict = {}

for i in range(len(input)):
  dict[input[i]] = output[i]

dict['z'] = 'q'

# load input

f = open(argv[1], 'r')
f.readline()
lines = f.readlines()

run = 1

#print sorted(dict.values())

for line in lines:
  
  ans = "".join(map(lambda x: dict[x], line.strip()))

  print "Case #" + str(run) + ": " + ans

  run+=1
