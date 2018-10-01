#!/usr/bin/env python

from sys import stdin, stderr

INF = 1000000000

def solve(S, K):
   N = len(S)
   res = 0
   for i in xrange(N-K+1):
      if S[i] == '-':
         res += 1
         T = ''.join( ['+' if c == '-' else '-' for c in S[i:i+K]] )
         S = S[:i] + T + S[i+K:]
   return res if S == '+' * N else INF

def main():
   TC = int(stdin.readline())
   for tc in xrange(1, TC+1):
      S, K = stdin.readline().split()
      K = int(K)
      res = solve(S, K)
      if res >= INF:
         print 'Case #%d: IMPOSSIBLE' % (tc)
      else:
         print 'Case #%d: %d' % (tc, res)
   return 0

if __name__ == '__main__': main()
