#! /usr/bin/env python2.7

import sys

#flip a series of pancakes
# takes string s
# takes index i
def flip(s,i,w):
  s=list(s)
  if i+w >= len(s):
    i=len(s)-w

  for l in range(0,w):
    if s[i+l]=='+':
      s[i+l]='-'
    else:
      s[i+l]='+'
  return ''.join(s)

#boolean return of whether the string is good or not
def completed(s):
  for c in s:
    if c!='+':
      return False
  return True

############################################
#Main execution
sample = int( sys.stdin.readline().strip() )
mcase = sample+1

while sample > 0:
  IN = sys.stdin.readline().split()

  #establish stack and width settings
  stack = IN[0]
  width = int(  IN[1] )
  #
  i=0
  flips=0
  while i < len(stack):
    if stack[i]!='+': 
      stack = flip(stack,i,width)
      flips += 1
      if completed(stack):
        break
    i+=1

  if not completed(stack):
    flips="IMPOSSIBLE"

  print "Case #{}: {}".format(mcase-sample,flips)

  sample-=1



