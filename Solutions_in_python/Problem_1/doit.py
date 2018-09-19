#!/usr/bin/python2.4

import sys

def runFor(engines, searches):
  switches = 0

  candidates = set(engines)
  for search in searches:
    candidates.discard(search)
    if not candidates:
      switches += 1
      candidates = set(engines)
      candidates.remove(search)

  return switches

def runCase():
  engine_count = int(sys.stdin.readline())
  engines = []
  for i in xrange(0, engine_count):
    engines.append(sys.stdin.readline().strip())
  search_count = int(sys.stdin.readline())
  searches = []
  for i in xrange(0, search_count):
    searches.append(sys.stdin.readline().strip())

  return runFor(engines, searches)

def main():
  cases = int(sys.stdin.readline())
  for case in xrange(0, cases):
    result = runCase()
    print "Case #%d: %d" % (case + 1, result)


main()
