#!/usr/bin/python

fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

T = int(fin.readline())

for i in range ( 1, T + 1 ):
  data = fin.readline().split(' ')
  N = int(data[0])
  S = int(data[1])
  p = int(data[2])
  scores = map(lambda j: int(j), data[3:])
  res = 0
  surprises = 0
  nosurprises = 0
  min_score = []
  if p == 0:
    res = len(scores)
  elif p == 1:
    for j in scores:
      if j > 0:
        res += 1
  else:
    min_score.append(p - 2 + p - 2 + p)
    min_score.append(p - 2 + p - 1 + p)
    for j in scores:
      if j == min_score[0] or j == min_score[1]:
        surprises += 1
      elif j > min_score[1]:
        nosurprises += 1
      else:
        pass
    res = surprises + nosurprises if S >= surprises else nosurprises + S
  fout.write('Case #%d: %d\n' % (i, res) )
  

