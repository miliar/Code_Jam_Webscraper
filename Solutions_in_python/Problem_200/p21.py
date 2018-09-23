def tidy(n):
  k = list(str(n))
  for i in range(1, len(k)):
    if k[i] < k[i-1]:
      return False
  return True

for i in range(int(input())):
  n = int(input())
  while True:
    if tidy(n):
      print(n)
      break
    else:
      n -= 1
  