file_in = open('a.in', 'r')
file_out = open('a.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  pancakes, k = file_in.readline().split()
  k = int(k)
  n = len(pancakes)

  a = [0] * n
  for i in range(n):
    if pancakes[i] is '+':
      a[i] = 1

  n_flips = 0
  impossible = False

  for i in range(n - k + 1):
    if a[i] is 0:
      for j in range(k):
        a[i+j] = 1 - a[i+j]
      n_flips += 1

  for i in range(n - k + 1, n):
    if a[i] is 0:
      impossible = True
      break

  file_out.write("Case #{}: ".format(t))
  if impossible:
    file_out.write('IMPOSSIBLE')
  else:
    file_out.write(str(n_flips))
  file_out.write('\n')