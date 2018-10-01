#!/usr/bin/env python

def solve(case_nr):
  result = 1
  
  slots = [None for i in xrange(1440)]
  
  [Ac,Aj] = map(int, raw_input().split())
  
  if (Ac>0) or (Aj>0):
    start = 1440
    total_C = 0
    total_J = 0
    for i in xrange(Ac):
      [C,D] = map(int, raw_input().split())
      start = min(start, C)
      total_C += (D-C)
      for j in xrange(C,D):
        slots[j] = 'C'

    for i in xrange(Aj):
      [C,D] = map(int, raw_input().split())
      start = min(start,C)
      total_J += (D-C)
      for j in xrange(C,D):
        slots[j] = 'J'

    #print slots
    
    transitions = 0
    free_to_allocate = 0
    sections = []
    i = start
    state = slots[start]
    for j in xrange(1440):
      i = (i+1) % 1440
      if ((state == 'C') or (state == 'J')):
        if (slots[i] == state):
          # No change
          pass
        elif (slots[i] == None):
          # Transfer to None section
          state = state+'N'
          section_length = 1
        else:
          transitions += 1
          state = slots[i]
      else:
        if (slots[i] == None):
          # No change
          section_length += 1
        elif (slots[i] == state[0]):
          # Found a section where a switch should only be placed to equal the times
          state = slots[i]
          sections.append(section_length)
        else:
          free_to_allocate += section_length
          transitions += 1
          state = slots[i]
    
    # Figure out if we need to do extra exchanges
    sections.sort()
    while ((total_C+free_to_allocate) < 720) or ((total_J+free_to_allocate) < 720):
      transitions += 2
      free_to_allocate += sections.pop()
      
  print "Case #%d: %d" % (case_nr, transitions)


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
