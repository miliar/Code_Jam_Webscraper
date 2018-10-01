import sys

L = [l.strip() for l in open(sys.argv[1]).readlines()]

i = 1
case = 0

while i < len(L):
  
  case += 1
  print "Case #%s:"%case,
  

  
  S = L[i+1:i+eval(L[i])+1]
  i += eval(L[i])+1
  Q = L[i+1:i+eval(L[i])+1]
  i += eval(L[i])+1
  #print S,'\n'
  #print Q
  sw = 0; idx = 0
  while idx != -1:
    try:
     idx += max([Q[idx:].index(s) for s in S])
     sw += 1
    except ValueError:
     break
  
  print sw