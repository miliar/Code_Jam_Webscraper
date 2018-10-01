def readLine():
  return [ int(x) for x in input().split() ];

for c in range(int(input())):
  Y, X = readLine();
  B = [ readLine() for y in range(Y) ];
  MX = [ max(B[y][x] for y in range(Y)) for x in range(X) ];
  MY = [ max(B[y][x] for x in range(X)) for y in range(Y) ];
  res = 'YES';
  for y in range(Y):
    for x in range(X):
      if B[y][x] != min(MX[x], MY[y]):
        res = 'NO';
  print('Case #', c+1, ': ', res, sep='');
