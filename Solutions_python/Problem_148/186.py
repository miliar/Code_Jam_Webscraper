#!/usr/bin/python3

T = int (input ())
for t in range (T):
  [N, X] = map (int, input ().split ())
  a = sorted (list (map (int, input ().split ())))
  ans = N
  i = 0
  j = len (a) - 1
  while i < len (a):
    while j > i and a[i] + a[j] > X:
      j -= 1
    if i < j:
      j -= 1
      ans -= 1
    i += 1
  print ('Case #' + str (t + 1) + ': ' + str (ans))
