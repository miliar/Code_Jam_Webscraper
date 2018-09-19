#!/usr/bin/python

def fas(n):
  l = long(n);
  ll = str(l*l);
  if (ll == ll[::-1]): print ll,"=",n;

print '1 = 1'
print '4 = 2'
print '9 = 3'

for dig in range(2,51):
  n = (dig+1) // 2;
  for B in range(1<<(n-1),1<<n):
    s = bin(B)[2:];
    if (dig%2 == 0): p = s + s[::-1];
    else: p = s[:-1] + s[::-1];
    fas(p)
    p2 = '2' + p[1:-1] + '2'; fas(p2);
    if (dig%2 == 1 and B%2==0): 
      p2 = s[:-1] + '2' + s[:-1][::-1]; fas(p2);
