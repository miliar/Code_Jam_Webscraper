import re
import sys

file = len(sys.argv)>1 and open(sys.argv[1]) or sys.stdin

L, D, N = map(int,file.readline().split())

def L_chars(s): return len(s)==L

dict = []

for i in xrange(D):
  dict.append(file.readline().strip())
  
dict_str = ' '.join(filter(L_chars,dict))

for i in xrange(N):
  re_str = file.readline().strip().replace('(','[').replace(')',']')
  matches = filter(L_chars,re.findall(re_str, dict_str))
  print "Case #%d: %d"%(i+1, len(matches))

