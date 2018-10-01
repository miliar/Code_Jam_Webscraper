T = int(input())
for testcase in range(1, T + 1):
  s = input()
  digit = []
  for c in s:
   digit.append(ord(c) - ord('0'))
  digit = digit[::-1]
  for i in range(len(digit) - 1):
    if digit[i] < digit[i + 1]:
      for j in range(i + 1):
        digit[j] = 9
      digit[i + 1] -= 1
  number = int(''.join([str(c) for c in digit][::-1]))
  if len(digit) > 1:
    number = max(number, int('9' * (len(digit) - 1)))
  print("Case #{}: {}".format(testcase, number))
