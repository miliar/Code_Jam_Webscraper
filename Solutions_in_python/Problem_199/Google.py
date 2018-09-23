t = int(input())

for _ in range(t):
  s = input()
  n = len(s)
  for i in range(n - 1, -1, -1):
    if (s[i] == ' '):
      l = n - i
      break
  k = int(s[-l::])
  s = s[:-l:]
  s = list(s)
  n = len(s)
  ans = 0
  for i in range(n - k + 1):
    if (s[i] == '-'):
      ans += 1
      for j in range(k):
        if (s[i + j] == '-'):
          s[i + j] = '+'
        else:
          s[i + j] = '-'
  for i in range(n):
    if (s[i] == '-'):
      ans = -1
  if (ans == -1):
    print('Case #', _ + 1, ': IMPOSSIBLE', sep = '')
  else:
    print('Case #', _ + 1, ': ', ans, sep = '')