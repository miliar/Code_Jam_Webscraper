#!/usr/bin/env python
#:%s/^\s\+print /#&/g
import sys

def readintsline():
  return map(int, raw_input().split())

def readfloatsline():
  return map(float, raw_input().split())

def float_as_string(f, decimals=7):
  return ("{:.%df}" % decimals).format(f)
  
def case_result(index, *args):
  sys.stderr.write("Case #%d: %s\n" % (index, ', '.join(args)))

def do_test_case():
  [max_shyness, shy_string] = raw_input().split()
  max_shyness = int(max_shyness)
#  print 'max_shyness: %d, shy_string: %s' % (max_shyness, shy_string)
  standing = 0
  friends = 0
  for i in range(max_shyness + 1):
    shy_i = int(shy_string[i])
#    print "i: %d, standing: %d" % (i, standing)
    if i <= standing:
      standing += shy_i
#      print "adding shy i: %d, standing is now: %d" % (shy_i, standing)
    else:
      added = i - standing
      friends += added
      standing += added + shy_i
#      print "adding %d friends, friends is now: %d, standing is now: %d" % (added, friends, standing)
  return str(friends)



def main():
  T = int(raw_input())
  for index in xrange(1, T + 1):
    case_result(index, do_test_case())

main()
#export PROG=./skeleton.py && mv ~/Downloads/*-small*.in . ; ./$PROG < *-small-*.in 2> small.out
#export PROG=./skeleton.py && mv ~/Downloads/*-large*.in . ; ./$PROG < *-large-*.in 2> large.out
