#!/usr/bin/env python
# (c) Christoph Grenz

from sys import stdin, stdout, stderr
from copy import copy

length = 0
words = set()
tests = []


def parseTest(line, x=-1):
  test = []
  currentgroup = None
  for c in line:
    if currentgroup is None:
      if c == '(':
        currentgroup = set()
      elif c == ')':
        raise ValueError('Syntax error in check %i' % x)
      else:
        test.append(c)
    else:
      if c == ')':
        test.append(frozenset(currentgroup))
        currentgroup = None
      elif c == '(':
        raise ValueError('Syntax error in check %i' % x)
      else:
        currentgroup.add(c)
  return test


def testPattern(pattern, words, wlen):
  def checkPattern(tmp):
    if len(tmp) == wlen:
      xy = ''.join(tmp)
      print >>stderr, 'Checking %s' % xy
      if xy in words:
        return 1
      else:
        return 0
    else:
      current_part = pattern[len(tmp)]
      if (isinstance(current_part, basestring)):
        return checkPattern(tmp+(current_part,))
      else:
        c = 0
        for x in current_part:
          for y in words:
            if y.startswith(''.join(tmp+(x,))):
              c += checkPattern(tmp+(x,))
              break
        return c
  return checkPattern(())

wlen, wordcount, testcount = stdin.readline().strip().split(' ', 2)
wlen = int(wlen)
wordcount = int(wordcount)
testcount = int(testcount)

for x in xrange(wordcount):
  word = stdin.readline().strip()
  if len(word) != wlen:
    raise ValueError('Word %i length does not match specification' % x)
  words.add(word);

for x in xrange(testcount):
  print >>stderr, 'Parsing pattern %s...' % x
  test = parseTest(stdin.readline().strip(), x)
  if len(test) != wlen:
    ValueError('Pattern %i length does not match word length specification' % x)
    
  print >>stderr, 'Checking pattern %s...' % x
  print 'Case #%i: %i' % (x+1, testPattern(test, words, wlen))
  print >>stderr, 'Done.';





