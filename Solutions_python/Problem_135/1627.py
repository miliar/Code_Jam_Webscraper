#!/usr/bin/env python

import sys

def read():
  content = ''
  for line in sys.stdin:
    content += line
  return content

def main():
  content = read()
  lines = content.split('\n')
  cases = int(lines[0])
  lines = lines[1:]
  for i in range(cases):
    sublines = lines[0:5]
    lines = lines[5:]
    ans1 = int(sublines[0])
    sols1 = [ int(x) for x in sublines[ans1].split(' ') ]
    sublines = lines[0:5]
    lines = lines[5:]
    ans2 = int(sublines[0])
    sols2 = [ int(x) for x in sublines[ans2].split(' ') ]
    sols = []
    for sol in sols1:
      if sol in sols2:
        sols.append(sol)
    print 'Case #%d:'%(i+1),
    if len(sols) == 1:
      print sols[0]
    elif len(sols) == 0:
      print 'Volunteer cheated!'
    else:
      print 'Bad magician!'

if __name__ == '__main__':
  main()
