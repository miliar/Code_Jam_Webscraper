n = int(input())

for i in range(n):
  j = int(input())
  k = j
  while(k >= 0):
    num = [int(d) for d in str(k)]
    flag = 0
    for index, d in enumerate(num, start = 0):
      if index < len(num) - 1 and d > num[index + 1]:
        flag = 1
        break
    if flag == 0:
      num = ''.join(str(x) for x in num)
      print('case #' + str(i + 1) + ': ' + (num))
      break
    split_arr = [int(x) for x in str(k)]

    multiplier = 0
    digit = 0

    for c in range(len(split_arr) - 1, 1, -1):
      #print(c)
      if split_arr[c] <= split_arr[c - 1]:
        multiplier += 1
        digit = split_arr[c]
      else: break
    if digit == 0:
      k = k - 1
    else: k = k - int(''.join(str(x) for x in split_arr[c:]))
    #print(k)