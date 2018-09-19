tn = int(raw_input())
for cn in range(tn):
  print 'Case #%d:' % (cn + 1),
  r1 = int(raw_input())
  m1 = [map(int, raw_input().split()) for _ in range(4)]
  r2 = int(raw_input())
  m2 = [map(int, raw_input().split()) for _ in range(4)]
  r1 -= 1
  r2 -= 1
  common = set(m1[r1]) & set(m2[r2])
  if len(common) == 0:
    print 'Volunteer cheated!'
  elif len(common) == 1:
    print list(common)[0]
  else:
    print 'Bad magician!'
    