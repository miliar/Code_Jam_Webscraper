#!/usr/bin/env python

import sys

motes = []

def solvehelp(solved, s):
  global motes
  op = 0
  maxop = len(motes)
  for i in range(solved, len(motes)):
    m = motes[i]
    #print '2: m', m, 's', s
    if m < s:
      s += m
      #print '3: m<s', 's', s
    else:
      maxop = min(maxop, len(motes)-i)
        #print '4: maxop', maxop
      while(maxop>0):
        op += 1
        maxop -= 1
        #print '5: op', op
        s = 2*s-1
        #print '5.1: s', s
        if m < s:
          s += m
          #print '5.2: s', s
          break
  #print '6: return op', op
  return op

def solve(fIn, fOut, testNum, runTests=[]):
  global motes

  line = fIn.readline()
  [a,n] = [int(x) for x in line.split()]
  line = fIn.readline()
  motes = [int(x) for x in line.split()]
  motes = sorted(motes)
  #print '1: a', a, 'motes', motes
  s = a
  op = solvehelp(0, s)

  if runTests and not testNum in runTests:
    return
  else:
    fOut.write('Case #' + str(testNum) + ': ')

  #print '4 : ans', op
  fOut.write(str(op))
  fOut.write('\n')
  return


def main():
  if len(sys.argv) < 2:
    print 'usage: python', sys.argv[0], '<input file> [<start test number> <end test number>]'
    print '       Note : run tests from <start test number> to <end test number> inclusive.'
    sys.exit(1)

  filename = sys.argv[1]
  fIn = open(filename)
  numTestCases=int(fIn.readline())

  start = 1
  end = numTestCases+1
  outfilename = filename+'.out'

  jobid = ''
  if len(sys.argv) == 5:
    start = int(sys.argv[2])
    end = int(sys.argv[3])+1
    jobid = sys.argv[4]
    outfilename = filename + '.out' + '.' + jobid
  
  fOut = open(outfilename, 'w')

  for i in xrange(1, end):
    print 'test ', i
    solve(fIn, fOut, i, range(start, end))
    
  fIn.close()
  fOut.close()
  
  if len(sys.argv) == 5:
    subprocess.call(["touch", ".done." + jobid])

  return


if __name__ == '__main__':
  main()


"""
def main(filename):
  fIn = open(filename)
  fOut = open(filename+'.out', 'w')
  numTestCases=int(fIn.readline())
  for i in xrange(1, numTestCases+1):
    solve(fIn, fOut, i)
    
  fIn.close()
  fOut.close()
  return


main('A-large-practice.in')
"""



