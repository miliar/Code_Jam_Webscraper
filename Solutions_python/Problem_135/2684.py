#!/usr/bin/python3

T = int (input ())
for t in range (T):
  res = ''
  can = [0 for i in range (16)]
  for i in range (2):
    l = int (input ())
    for k in range (4):
      cl = [int (x) for x in input ().split ()]
      if l == k + 1:
        for j in range (4):
          can[cl[j] - 1] += 1
  ans = []
  for i in range (16):
    if can[i] == 2:
      ans += [i]
  if len (ans) == 0:
    res = 'Volunteer cheated!'
  elif len (ans) > 1:
    res = 'Bad magician!'
  else:
    res = str (ans[0] + 1)
  print ('Case #{0}: {1}'.format (t + 1, res))
