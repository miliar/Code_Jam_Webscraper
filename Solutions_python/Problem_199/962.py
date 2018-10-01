x = int(input())
for num in range(1, x + 1):
  curr = input()
  cakes = list(curr.split(' ')[0])
  flip = int(curr.split(' ')[1])
  flips = 0
  for i in range(0, len(cakes) - flip + 1):
    if cakes[i] == '-':
      for j in range(0, flip):
        if cakes[i + j] == '-':
          cakes[i + j] = '+'
        else:
          cakes[i + j] = '-'
      flips += 1
  if '-' in cakes:
    print("Case #" + str(num) + ": IMPOSSIBLE")
  else:
    print(("Case #" + str(num) + ": " + str(flips)))
