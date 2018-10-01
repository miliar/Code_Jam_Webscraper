"""
newmax = max(oldmax/2, secondmax)

while levelchosen_size >= oldmax/2
  if oldmax - newmax >= oldsize:
    split
    break
  else: try using next level as well
"""

import sys
import heapq

output_line = "Case #{X:d}: {minutes:d}"



def fastest_pancakes(pancakes):
    largest = max(pancakes)
    possible = [largest]
    if largest <= 2:
        return largest
    newpancakes = pancakes[:]
    newpancakes.remove(largest)
    newpancakes.extend([largest // 2, (largest + 1) // 2])
    possible.append(fastest_pancakes(newpancakes) + 1)

    if largest == 9:
        newpancakes = pancakes[:]
        newpancakes.remove(largest)
        newpancakes.extend([3, 3, 3])
        possible.append(fastest_pancakes(newpancakes) + 2)
    return min(possible)

if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            D = int(inhandle.readline())
            plates = list(map(int, inhandle.readline().split()))

            outline = output_line.format(X=t + 1, minutes=fastest_pancakes(plates))
            print(outline, file=outhandle)
            print(outline)
            print()



