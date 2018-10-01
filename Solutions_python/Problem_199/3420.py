test_cases = int(raw_input())

global count

def calc (cake, flipper):
  global count
  try:
    j = cake.index("-")
  except:
    j = len(cake)
  itterations = 0
  while j <= len(cake) - flipper and itterations < len(cake):
    itterations += 1
    if cake[j:j+1] != "+":
      count += 1
      for k in xrange(0, flipper):
        if cake[j+k:j+k+1] == "+":
          cake = cake[:j+k] + cake[j+k:].replace("+", "-", 1)
        else:
          cake = cake[:j+k] + cake[j+k:].replace("-", "+", 1)
      try:
        j = cake.index("-")
      except:
        j = len(cake)
    else:
      j += 1
  if "-" in cake:
    return "IMPOSSIBLE"
  return count



for i in xrange(1, test_cases + 1):
  count = 0
  cake, flipper = [s for s in raw_input().split(" ")]
  flipper = int(flipper)
  print "Case #{}: {}".format(i, calc(cake, flipper))
