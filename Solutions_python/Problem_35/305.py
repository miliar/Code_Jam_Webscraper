#!/usr/bin/env python2.6
# Watersheds (90101.1)
# A submission by Cortland Klein <me@pixelcort.com>
# 2009-09-03

# import pdb; pdb.set_trace();

from pdb import set_trace;
import re;


with open('B-large.in.txt') as f:
  t = int(f.next())
  
  for i in range(t):
    h, w = f.next().split(' ')
    w = int(w)
    h = int(h)
    
    matrix = []
    for j in range(h):
      row_cells = f.next().split(' ')
      row_cells = [{'altitude':int(cell)} for cell in row_cells]
      matrix.append(row_cells)
    
    # Generate an alphabet for this matrix
    alphabet = [chr(alphabetIter) for alphabetIter in xrange(ord('a'), ord('z')+1)]
    # Got alphabet snippet from http://www.gossamer-threads.com/lists/python/python/673502#673502
    
    # alphabet.pop(0) to get next letter
    
    def attemptToLabelCell (y,x):
      currentCell = matrix[y][x]
      # Only do work on unlabeled cells
      if not 'label' in currentCell:
        # Discover the direction to go
        currentAlt = currentCell['altitude']
        upAlt    = (0 <= y-1 < h and [matrix[y-1][x]['altitude']] or [9999999])[0]
        leftAlt  = (0 <= x-1 < w and [matrix[y][x-1]['altitude']] or [9999999])[0]
        rightAlt = (0 <= x+1 < w and [matrix[y][x+1]['altitude']] or [9999999])[0]
        downAlt  = (0 <= y+1 < h and [matrix[y+1][x]['altitude']] or [9999999])[0]
        
        minimumAlt = min(currentAlt, upAlt, leftAlt, rightAlt, downAlt)
        
        if currentAlt == minimumAlt:
          direction = 'sink'
        elif upAlt == minimumAlt:
          direction = 'up'
        elif leftAlt == minimumAlt:
          direction = 'left'
        elif rightAlt == minimumAlt:
          direction = 'right'
        elif downAlt == minimumAlt:
          direction = 'down'
        
        # If we're at a sink, label it and return the label
        if direction == 'sink':
          label = alphabet.pop(0)
          matrix[y][x]['label'] = label
          return label
        elif direction == 'up':    return attemptToLabelCell(y-1,x)
        elif direction == 'left':  return attemptToLabelCell(y,x-1)
        elif direction == 'right': return attemptToLabelCell(y,x+1)
        elif direction == 'down':  return attemptToLabelCell(y+1,x)
          
      else:
        # This cell already has a label; just return it.
        return matrix[y][x]['label']
      
    
    print "Case #" + str(i+1) + ":"
    # Loop through the matrix, from left to right then top to bottom
    for y in range(h):
      for x in range(w):
        # print str(i+1) + ": " + str(y) + "." + str(x) + ": " + str(matrix[y][x]['altitude'])
        label = attemptToLabelCell(y,x)
        print label + ' ',
      print ''

