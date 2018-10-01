import fileinput
import sys
import heapq
import math

myfile = fileinput.input();
maxcases = 0
currentcase = 0

def minFlips( maxheap ):
	# print maxheap	
	currentmax = heapq.heappop(maxheap)
	if (currentmax <= 3):
		return currentmax
	biggerhalf = int(math.ceil(currentmax/2.0))
	smallerhalf = currentmax - biggerhalf
	maxheap2 = maxheap[:]
	heapq.heappush(maxheap, smallerhalf)
	heapq.heappush(maxheap, biggerhalf)
	heapq._heapify_max(maxheap)

	biggerhalf += 1
	smallerhalf = currentmax - biggerhalf
	heapq.heappush(maxheap2, smallerhalf)
	heapq.heappush(maxheap2, biggerhalf)
	heapq._heapify_max(maxheap2)

	return min(currentmax, minFlips(maxheap)+1, minFlips(maxheap2)+1)

for line in myfile:

	if fileinput.isfirstline():
		maxcases = int(line.strip())
		continue

	initialdiners = int(line.strip())
	line = myfile.readline().strip()

	dinerPlates = [int(s) for s in line.split()]

	heapq._heapify_max(dinerPlates)

	currentcase += 1;
	sys.stdout.write("Case #"+str(currentcase)+": ")	
	sys.stdout.flush()

	print minFlips(dinerPlates)

	if maxcases == currentcase:
		break
