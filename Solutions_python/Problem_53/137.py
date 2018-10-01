count = int(raw_input())
for i in range(count):
  N, K =  [int(s) for s in raw_input().split(" ")]
  x = 2**N
  b = K % x == x - 1
  print 'Case #' + str(i+1)  + ': ' + ("ON" if b else "OFF")
