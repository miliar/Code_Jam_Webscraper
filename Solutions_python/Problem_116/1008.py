#!/usr/bin/env python

import sys

#convert = {'O': , 'X':, '.': , 'T':}

def calc(arr):
  dot_found = False

  beg = ''
  for w in range(4):
    if arr[w][w] == '.':
      break
    if arr[w][w] == 'T':
      if w==3:
        return "%s won" % (beg)
    if arr[w][w] in ['O', 'X']:
      if beg == '':
        beg = arr[w][w]
      else:
        if beg == arr[w][w]:
          if w == 3:
            return "%s won" % (beg)
        else:
          break
  beg = ''
  for w in range(4):
    if arr[3-w][w] == '.':
      break
    if arr[3-w][w] == 'T':
      if w==3:
        return "%s won" % (beg)
    if arr[3-w][w] in ['O', 'X']:
      if beg == '':
        beg = arr[3-w][w]
      else:
        if beg == arr[3-w][w]:
          if w == 3:
            return "%s won" % (beg)
        else:
          break


  for w in range(4):
    if '.' in arr[w]:
      dot_found = True
    # check horizontal
    beg = ''
    beg2 = ''

    for a in range(4):
      if arr[a][w] == '.':
        break
      if arr[a][w] == 'T':
        if a==3:
          return "%s won" % (beg2)
      if arr[a][w] in ['O', 'X']:
        if beg2 == '':
          beg2 = arr[a][w]
        else:
          if beg2 == arr[a][w]:
            if a == 3:
              return "%s won" % (beg2)
          else:
            break
    #import pdb; pdb.set_trace()

    for a in range(4):
      if arr[w][a] == '.':
        break
      if arr[w][a] == 'T':
        if a==3:
          return "%s won" % (beg)
      if arr[w][a] in ['O', 'X']:
        if beg == '':
          beg = arr[w][a]
        else:
          if beg == arr[w][a]:
            if a == 3:
              return "%s won" % (beg)
          else:
            break
  if dot_found:
    return "Game has not completed"
  else:
    return "Draw"

def get_array(ifile):
  return [[s for s in ifile.readline()][:-1] for i in range(4)]

ifile = open(sys.argv[1])
ofile = sys.stdout
for i in range(int(ifile.readline())):
  print "Case #%i: %s" % (i+1, calc(get_array(ifile)))
  try:
    ifile.readline()
  except:
    pass
