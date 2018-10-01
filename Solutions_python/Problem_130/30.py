T = int(raw_input())

def first_loss(pos, num):
  floss = 1
  while pos <= num/2:
    floss = floss + 1
    num = num / 2
  return floss

def first_win(pos, num):
  fwin = 1
  while num > 1 and pos > num/2:
    fwin = fwin + 1
    num = num / 2
    pos = pos - num
  return fwin
  
for test in range(T):
  N, P = map(int, raw_input().split())
  num = 2**N
  if P == num:
    print 'Case #' + str(test+1) + ':', num-1, num-1
    continue
  floss = first_loss(P+1, num)
  fwin = first_win(P, num)
  #print fwin, floss
  print 'Case #' + str(test+1) + ':', min(2**fwin - 2, num - 1), num - 1 - (2**floss - 1)