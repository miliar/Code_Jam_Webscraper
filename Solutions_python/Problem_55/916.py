for c in xrange(0, input()):
  revenue = 0
  rides_per_day, max_people, group_count = map(int, raw_input().split())
  groups = map(int, raw_input().split())
  
  i = 0 
  while i < rides_per_day:
    riders = j = 0
    while riders < max_people and j < group_count:
      if riders + groups[j] > max_people:
        break
      riders += groups[j]
      j += 1
    i += 1
    revenue += riders
    swap = groups[:j]
    groups = groups[j:] + swap
  print 'Case #%s: %s' % (c+1, revenue)
    
