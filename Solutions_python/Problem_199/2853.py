import sys

fname = sys.argv[1]
output = open(sys.argv[1] + ".out", 'w')

def solve(S, K):
  S = S.strip()
  flipper = int(K)

  pancake = map(lambda p: True if p =='+' else False, S)
  count = 0

  for i in range(0, len(pancake) - flipper + 1):
    if not pancake[i]:
      for j in range(0, flipper):
        pancake[i+j] = not pancake[i+j]
      count += 1

  if all(pancake):
    return count
  else:
    return "IMPOSSIBLE"

with open(fname) as f:
    content = f.readlines()

line = [x.strip() for x in content]

for i in range(1, int(line[0]) + 1):
  output.write("Case #" + str(i) + ": " + str(solve(*line[i].split(" "))) + "\n")
