#!/usr/bin/env python
import os
import sys
import time

tStart = time.time()

#---------------------------------------------------------------------

ifilename = 'input.in'
ofilename = 'results.out'

args = sys.argv
if len(args) > 1:
  ifilename = args[1]
if len(args) > 2:
  ofilename = args[2]

#---------------------------------------------------------------------
 
ifile = open(ifilename,'r')
data  = ifile.read()
ifile.close()
lines = data.splitlines()

ofile = open(ofilename, 'w')

#---------------------------------------------------------------------
# Functions


def get_sol(N,K):

  key = (N,K)
  try:
    return get_sol.cache[key]
  except:
    pass

  if K == N:
    sol = [0,0]

  elif [K,N] == [1,2]:
    sol = [0,1]

  elif [K,N] == [1,3]:
    sol = [1,1]
  
  elif [K,N] == [2,3]:
    sol = [0,0]

  elif K == 1:
    if N%2 == 1:
      sol = [N/2,N/2]
    else:
      sol = [N/2-1,N/2]
  
  else:
    N1 = N/2 - int(N%2==0)
    N2 = N/2

    K -= 1
    K1 = K/2
    K2 = K/2 + K%2    
    if K1 == 0:
      sol = get_sol(N2,K2)
    else:
      sol1 = get_sol(N1,K1)
      sol2 = get_sol(N2,K2)
      if (sol1[0] < sol2[0]) or (sol1[0] == sol2[0] and sol1[1] < sol2[1]):
        sol = sol1
      else:
        sol = sol2

#      if N1 < N2:
#        K1 -= 1
#        K2 += 1
#        if K1 == 0:
#          sol3 = get_sol(N2,K2)
#        else:
#          sol1 = get_sol(N1,K1)
#          sol2 = get_sol(N2,K2)
#          if (sol1[0] < sol2[0]) or (sol1[0] == sol2[0] and sol1[1] < sol2[1]):
#            sol3 = sol1
#          else:
#            sol3 = sol2
#        if (sol[0] < sol3[0]) or (sol[0] == sol3[0] and sol[1] < sol3[1]):
#          sol = sol3

  get_sol.cache[key] = sol
  return sol

get_sol.cache = {}

#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  data  = lines[0].split()
  lines = lines[1:]
  N     = int(data[0])
  K     = int(data[1])
  solution = get_sol(N,K)
  solution = '%d %d'%(solution[1], solution[0])


  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
