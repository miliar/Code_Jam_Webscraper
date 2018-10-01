#! /usr/bin/env python2.7

import sys

def is_tidy( vals ):
  i = len(vals)-1
  while i > 0:
    if vals[i-1] > vals[i]:
      return False
    i -= 1

  return True

def is_untidy( num ):
  num.reverse()
  if is_tidy( num ):
    num.reverse()
    return True
  else:
    num.reverse()
    return False


#decrement number represented by list of caracters
def decrement( num ):
  carry = False
  if num[-1] == '0':
    carry=True
    num[-1] = '9'
  else:
    num[-1]=str( int(num[-1])-1 )
  #
  i=-2
  while carry:
   if num[i] == '0':
      carry=True
      num[i] = '9'
   else:
      num[i] = str( int(num[i])-1 )
      carry=False

   i -= 1
  #
  while num[0]=='0':
    num.pop(0)
 
  return num


def tidy(ciel):
  while ciel > 0:
    if is_tidy( ciel ):
      return ciel
    elif is_untidy( ciel ):
      if ciel[0]=='1':
        ciel = list( '9'*(len(ciel)-1) )
      else: 
        ciel = [ str( int(ciel[0])-1 ) ]+list( '9'*(len(ciel)-1) )
    elif  ciel[0] < ciel[1]:
      ciel = list(ciel[0]) + tidy(ciel[1:])
    else:
      ciel = decrement(ciel)



############################################
#Main execution
sample = int( sys.stdin.readline().strip() )
mcase = sample+1

while sample > 0:
  m = sys.stdin.readline().strip()

  max_t = ''.join( tidy( list(m) ) ) 

  print "Case #{}: {}".format(mcase-sample,max_t)

  sample-=1



