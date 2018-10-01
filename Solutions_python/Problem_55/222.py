for case in xrange(1, int(raw_input())+1):
  R, k, N = map(int, raw_input().split())
  G = map(int, raw_input().split())

  jump = []
  pointer = 0
  people = 0
  for i in xrange(N):
    while people + G[pointer] <= k and (pointer != i or people == 0):
      people += G[pointer]
      pointer = (pointer+1) % N
    jump.append((pointer, people))
    people -= G[i]

  income = 0
  pointer = 0
  for _ in xrange(R):
    income += jump[pointer][1]
    pointer = jump[pointer][0]

  print "Case #%d: %d" % (case, income)
