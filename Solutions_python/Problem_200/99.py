_T = int(raw_input())
for _t in range(1, _T+1):
  N = map(int, list(raw_input()))
  for _ in range(len(N)):
    for i in range(len(N) - 1):
      if N[i+1] < N[i]:
        for j in range(i+1, len(N)):
          N[j] = 9
        N[i] -= 1
        break
  res = int(''.join(map(str, N)))

  print 'Case #{}: {}'.format(_t, res)
