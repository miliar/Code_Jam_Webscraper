
import sys

def valid(chars):
   a = None
   players = 'XO'
   for c in chars:
      if c in players and a is None:
         a = c
      elif c == 'T':
         continue
      elif c != a:
         return None
   return a

def check(lines):
   complete = True
   # Check rows and columns
   for i in xrange(4):
      if '.' in lines[i]:
         complete = False
      r = valid(lines[i]) or valid([lines[j][i] for j in xrange(4)])
      if r:
         return r
   # Check diagonals
   r = valid([lines[j][j] for j in xrange(4)]) or valid([lines[j][3-j] for j in xrange(4)])
   if r:
      return r
   if complete:
      return 'D'
   else:
      return 'I'

def main():
   N = int(raw_input())
   print >> sys.stderr, 'N = %d' % (N,)
   results = {'X': 'X won', 'O': 'O won',
         'D': 'Draw', 'I': 'Game has not completed'}
   for t in xrange(N):
      lines = []
      for i in xrange(4):
         lines.append(raw_input().strip())
      print 'Case #%d: %s' % (t+1, results[check(lines)])
      raw_input() # Clear blank lines between

if __name__ == '__main__':
   main()
