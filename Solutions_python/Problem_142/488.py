for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  N = int(raw_input())
  s = []
  for i in xrange(N):
    s.append(raw_input())
  index = [0] * N
  num = 0
  match = True
  end = False
  while True:
    for i in range(N-1):
      if s[i][index[i]] != s[i+1][index[i+1]]:
        match = False
        break
    if not match:
      break
    run = [1] * N
    for i in range(N):
      for j in range(index[i]+1, len(s[i])):
        if s[i][j] != s[i][j-1]:
          break
        run[i] += 1
      index[i] += run[i]
      if index[i] == len(s[i]):
        end = True
    avg1, avg2 = sum(run)/N, sum(run)/N + 1
    num1, num2 = 0, 0
    for i in range(N):
      num1 += abs(run[i]-avg1)
      num2 += abs(run[i]-avg2)
    num += min(num1, num2)
    if end:
      for i in range(N):
        if index[i] != len(s[i]):
          match = False
          break
      break
  if match:
    print num
  else:
    print "Fegla Won"

