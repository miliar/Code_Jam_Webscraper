#!/usr/bin/python
import sys
if __name__ == '__main__':
  f = open(sys.argv[1])
  for i in xrange(int(f.readline())):
    print ('Case #%d:' % (i + 1)),
    N, K = map(int, f.readline().strip().split())
    print 'ON' if K % (2 ** N) == 2 ** N - 1 else 'OFF'
