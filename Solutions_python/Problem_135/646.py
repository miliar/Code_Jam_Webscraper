ntc = input()
for itc in range(ntc):
  possible = set(range(1, 17))
  for _ in range(2):
    row = input() - 1
    for i in range(4):
      for val in map(int, raw_input().split()):
        if i != row and val in possible:
          possible.remove(val)
  if not possible:
    res = 'Volunteer cheated!'
  elif len(possible) > 1:
    res = 'Bad magician!'
  else:
    res = possible.pop()
  print 'Case #{0}: {1}'.format(itc+1, res)


