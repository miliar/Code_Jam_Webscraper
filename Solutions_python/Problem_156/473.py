from collections import deque
from copy import copy
import bisect

class sortedlist(list):
	'''just a list but with an insort (insert into sorted position)'''
	def insort(self,x):
	    self=bisect.insort(self,x)		

def reduce_by_one(l):
	new_list = sortedlist()
	for n in l:
		if n > 1:
			new_list.insort(n - 1)
	return new_list

with open('B-small-attempt2.in') as f:
	with open('B-small-attempt2.out','w') as of: 
		n = int(f.readline())
		for j in range(n):
			print(j)
			initialList = sortedlist()
			f.readline()
			for num in f.readline().split(" "):
				initialList.insort(int(num))
			queue = deque([(initialList, 0)])
			seen = set()
			while True:
				plates, mins = queue.popleft()
				if tuple(plates) in seen:
					continue
				seen.add(tuple(plates))
				if len(plates) == 0:
					of.write("Case #{}: {}\n".format(j+1,mins))
					break
				if plates[-1] > 3:
					for k in range(2,plates[-1] // 2 + 1):
						nl = copy(plates)
						nl[-1] -= k
						nl.sort()
						nl.insort(k)
						queue.append((nl,mins + 1))
				queue.append((reduce_by_one(plates),mins + 1))