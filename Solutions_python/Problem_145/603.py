#!/bin/python
problem='A'


import sys
import math

def solve(p,q):
  if p>q:
    return -1
  if p==q:
    return 0
  for i in xrange(2,min(p,int(math.sqrt(q)))+1):
    while p%i==0 and q%i==0:
      p/=i
      q/=i

  lq=0
  while q>1:
    if q%2:
      return -1
    lq+=1
    q/=2
  lp=0
  while p>1:
    lp+=1
    p/=2

  return lq-lp


def doall(outf, testcases, lines):
  case = 1

  while lines:
    p,q = [int(x.strip()) for x in lines[0].split('/')]
    lines=lines[1:]
 
    s=solve(p,q)
    if s<0:
      s='impossible'
    else:
      s=str(s)
    print >> outf, 'Case #%d: %s'%(case,s)

    case+=1


def readin(infile):
  print >> sys.stderr, "reading from " + infile
  lines=open(infile, 'r').readlines()
  testcount = int(lines[0])
  print >> sys.stderr, "read %d test cases from %d lines"%(testcount, len(lines))
  lines=lines[1:]
  return testcount, lines

if __name__ == '__main__': 
  if len(sys.argv) == 1:
    inf='A-test.in'
    outf=sys.stdout
    print >> sys.stderr, "writing to stdout "
  elif len(sys.argv) == 3:
    input_name_format='{problem}-{input}-{id}.in'
    output_name_format='{problem}-{input}-{id}.out'

    inf=str.format(input_name_format, problem=problem, input=sys.argv[1], id=int(sys.argv[2]))
    outf=str.format(output_name_format, problem=problem, input=sys.argv[1], id=int(sys.argv[2]))
    print >> sys.stderr, "writing to "+outf
    outf = open(outf,'w')
  else:
    print >> sys.stderr, "bad args"
    sys.exit(1)
  tc, l = readin(inf)
  doall(outf, tc, l)
  print >> sys.stderr, "done"

