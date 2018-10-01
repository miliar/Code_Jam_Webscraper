import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
  n = sys.stdin.readline()
  num = [int(s) for s in list(n.strip('\n'))]
  j = 0
  while j < len(num) - 1:
      if num[j] > num[j+1]:
          for k in range(j+1, len(num)):
              num[k] = 9
          num[j] = num[j] - 1
          j = 0
      else:
          j = j + 1

  while num[0] == 0:
      num.pop(0)

  ans = ''.join(str(s) for s in num)
  print("Case #{}: {}".format(i, ans))
