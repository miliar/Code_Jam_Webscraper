#!/usr/bin/env python

def check_tidy(nstr):
  for i,c in enumerate(nstr):
    if i==0:
      continue
    if nstr[i]<nstr[i-1]:
      return i 
  return "TIDY" 

def make_tidy(nstr):
  case = check_tidy(nstr) 
  if case=="TIDY":
    return nstr

  else:
    nstr=nstr[0:case]+str(9)+"9"*len(nstr[case+1:])

    #print "prev case", nstr[case-1]
    if nstr[case-1] != "0":
      nstr=nstr[0:case-1]+str(int(nstr[case-1])-1)+"9"*len(nstr[case:])
    else:
      #print "is a zero"
      nstr=nstr[0:case-1]+str(9)+nstr[case:]

    #print "debug",nstr
    return make_tidy(nstr)
    
cases = raw_input()
for c in range(int(cases)):
    n=raw_input().strip()
    a=int(make_tidy(n))
    print "Case #%i: %s" % ( (c+1), a)
