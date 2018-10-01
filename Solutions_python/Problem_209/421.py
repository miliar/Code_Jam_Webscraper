import sys
import math

def solve(N, K, pancakes):
  bestArea = 0;

  if K == 1:
    totalAreaSorted = list(reversed(sorted(pancakes, key=lambda tup: tup[3])))
    return totalAreaSorted[0][3]

  radiusSorted = list(reversed(sorted(pancakes, key=lambda tup: tup[0])))

  for i in range(N-1):
    selectedBase = radiusSorted[i]
    remainingPancackes = list(radiusSorted[i+1:])

    areaSorted = list(reversed(sorted(remainingPancackes, key=lambda tup: tup[2])))
    # print areaSorted
    if len(areaSorted) < K-1:
      break;

    selectedPancakes = areaSorted[0:K-1]

    totalArea = math.pi * selectedBase[0] * selectedBase[0] + selectedBase[2];

    for p in selectedPancakes:
      totalArea += p[2]

    if totalArea > bestArea:
      bestArea = totalArea

  return bestArea

t = int(raw_input())
for i in range(1, t + 1):

  
  N, K = map(int,[s for s in raw_input().split(" ")])

  pancakes = []

  for p in range(N):
    r, h = map(float,[s for s in raw_input().split(" ")])
    lateralArea = 2 * math.pi * r * h
    totalArea = lateralArea + math.pi * r * r

    pancakes.append([r, h, lateralArea, totalArea])

  result = solve(N, K, pancakes)
  
  # print result

  print("Case #{0:d}: {1:.9f}".format(i, result))
  sys.stdout.flush()