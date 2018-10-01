def num_flips(s, K):
  num_cakes = len(s)
  i = 0
  cnt_flips = 0
  for i in range(num_cakes - K + 1):
    if s[i]:
      continue
    for j in range(i, i + K):
      s[j] = not s[j]
    cnt_flips += 1

  for i in range(num_cakes - K + 1, num_cakes):
    if not s[i]:
      return "IMPOSSIBLE"
  return cnt_flips


num_tests = int(input())
for test_id in range(1, num_tests + 1):
  tmp = input().split(" ")
  assert len(tmp) == 2
  s = [ch == "+" for ch in tmp[0]]
  K = int(tmp[1])
  result = num_flips(s, K)
  print("Case #{0}: {1}".format(test_id, result))

