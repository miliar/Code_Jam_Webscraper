def intersect(a, b):
  return list(set(a) & set(b))

T = int(raw_input())
for i in xrange(T):
  row_num = int(raw_input())

  row1 = []
  row2 = []

  for j in xrange(4):
    row = raw_input()
    if j + 1 == row_num:
      row1 = map(int, row.split(" "))

  row_num = int(raw_input())

  for j in xrange(4):
    row = raw_input()
    if j + 1 == row_num:
      row2 = map(int, row.split(" "))

  common = intersect(row1, row2)

  print "Case #" + str(i + 1) + ":",
  if len(common) == 1:
    print common[0]
  elif len(common) > 1:
    print "Bad magician!"
  else:
    print "Volunteer cheated!"