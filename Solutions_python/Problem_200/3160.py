import sys

def dec(num):
  i = len(num) - 1
  while i > 0:
    if num[i] < num[i - 1]:
      for j in range(i, len(num)):
        num[j] = 9
      num[i - 1] -= 1
    i -= 1
  return num

def to_str(num):
  skipping = True
  i = 0
  result = ''
  while i < len(num):
    if skipping:
      if num[i] > 0:
        skipping = False
        result += str(num[i])
    elif not skipping:
        result += str(num[i])
    i += 1
  return result

lines = sys.stdin.readlines()
lines.pop(0)
i = 1
for line in lines:
  num = [int(x) for x in line.strip()]
  print 'Case #{}: {}'.format(i, to_str(dec(num)))
  i += 1

