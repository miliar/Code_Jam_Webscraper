dicti = {'+':'-', '-':'+'}

for tc in range(input()):
  flips = 0
  pancakes, size = raw_input().split(" ")
  listed_input = list(pancakes)
  size = int(size)
  for i in range(len(listed_input) - size + 1):
    if listed_input[i] == '-':
      for x in range(size):
        listed_input[i+x] = dicti[listed_input[i+x]]
      flips = flips + 1
  if listed_input.count('-') > 0:
    flips = "IMPOSSIBLE"
  else: flips = str(flips)
  print "Case #" + str(tc + 1) + ": " + flips