T = int(raw_input().strip())

for case_n in range(1, T+1):
  g1 = int(raw_input().strip()) - 1
  b1 = [map(int, raw_input().strip().split()) for line in range(4)]
  g2 = int(raw_input().strip()) - 1
  b2 = [map(int, raw_input().strip().split()) for line in range(4)]
  s1, s2 = set(b1[g1]), set(b2[g2])
  diff = s1 & s2
  if len(diff) == 1:
    result = str(list(diff)[0])
  elif len(diff) > 1:
    result = "Bad magician!"
  else:
    result = "Volunteer cheated!"
  print("Case #{0}: {1}".format(case_n, result))
