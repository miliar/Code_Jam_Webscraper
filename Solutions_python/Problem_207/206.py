file_in = open('B-small-attempt1.in')
file_out = open('B-small-attempt1.out', 'w')

T = int(file_in.readline())

def check(ans):
  for i in range(len(ans)):
    if ans[i - 1] == ans[i]: return False
  return True

for t in range(1, T+1):
  N, R, O, Y, G, B, V = map(int, file_in.readline().split())

  col = [R, Y, B]
  c = ['R', 'Y', 'B']

  m = max(col)
  s = R+Y+B
  ans = ''
  if m * 2 > s: ans = 'IMPOSSIBLE'
  else:
    last = ''
    for i in range(N):
      m1, m2 = -1, -1
      for j in range(3):
        if m1 < 0 or col[j] > col[m1]:
          m2 = m1
          m1 = j
        elif m2 < 0 or col[j] > col[m2]:
          m2 = j
      # print(c[m1], last)
      if c[m1] == last:
        # print('wtf', c[m1], last)
        ans += c[m2]
        last = c[m2]
        col[m2] -= 1
      else:
        ans += c[m1]
        last = c[m1]
        col[m1] -= 1
      # print(c[m1], c[m2], ans, last)

  if ans != 'IMPOSSIBLE':
    if not check(ans):
      ans = ans[0:-2] + ans[-1] + ans[-2]
      # print(N, R, Y, B, ans)
      # if not check(ans): print('fuck')

  file_out.write('Case #' + str(t) + ': ' + ans + '\n')
