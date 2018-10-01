#!/usr/bin/python4
import string
fname = '/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/2012/small'
objfile = open('%s.in' % fname, 'r')
counter = -1
result = []
output = ''
num = 0

Googlerese = {}
Googlerese[' '] = ' '
Googlerese['a'] = 'y'
Googlerese['b'] = 'h'
Googlerese['c'] = 'e'
Googlerese['d'] = 's'
Googlerese['e'] = 'o'
Googlerese['f'] = 'c'
Googlerese['g'] = 'v'
Googlerese['h'] = 'x'
Googlerese['i'] = 'd'
Googlerese['j'] = 'u'
Googlerese['k'] = 'i'
Googlerese['l'] = 'g'
Googlerese['m'] = 'l'
Googlerese['n'] = 'b'
Googlerese['o'] = 'k'
Googlerese['p'] = 'r'
Googlerese['q'] = 'z'
Googlerese['r'] = 't'
Googlerese['s'] = 'n'
Googlerese['t'] = 'w'
Googlerese['u'] = 'j'
Googlerese['v'] = 'p'
Googlerese['w'] = 'f'
Googlerese['x'] = 'm'
Googlerese['y'] = 'a'
Googlerese['z'] = 'q'

for ln in objfile.readlines():
  counter += 1
  if not counter:
    continue
  if not num:
    num = int(ln.replace('\n', ''))
    counter -= 1 
    continue
  for letters in ln:
    for i in letters:
      output += Googlerese[i]
    
  result.append('Case #%s: %s' % output)
  num = 0
  output = ''
  
objfile.close()
objfile = open('/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/2012/test.out', 'w')
objfile.write(string.join(result, '\n'))
objfile.close()
