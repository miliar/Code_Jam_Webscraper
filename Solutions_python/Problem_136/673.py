Z = int(input())
for z in range(1, Z + 1):
  C, F, X = map(float, input().split())
  minT = X / 2.0
  t, r = 0.0, 2.0
  while t < minT:
    t += C / r
    r += F
    tmpT = t + X / r
    if tmpT <= minT:
      minT = tmpT
  print("Case #{}: {}".format(z, minT))
