import math
import sys
sys.setrecursionlimit(1000000000)

def kth_neighbours(partitions,k):
	# print k, partitions
	sel = 0
	best_p = partitions[0][0]
	# print best_p
	temp_index = 1
	for p,i,j in partitions[1:]:
		if p > best_p:
			best_p = p
			sel = temp_index
		temp_index += 1
	(p, i, j) = partitions[sel]
	diff = (j-i)/2 + i
	if k == 1:
		d1 = diff - i
		d2 = j - diff
		min_d = min(d1,d2)
		max_d = max(d1,d2)
		return (max_d, min_d)
	
	new_parts = []
	if diff != i:
		new_parts.append(((diff - 1) -i, i, diff - 1))
	if diff != j:
		new_parts.append((j - (diff+1), diff + 1, j))
	partitions = partitions[:sel] + new_parts + partitions[sel+1:]
	return kth_neighbours(partitions, k-1)
			
		
def bathroom_partition(power, n, e, k, acc):
	# x = int(math.pow(2,power))
	q = (n-e)/e
	r = (n-e)%e
	if k <= (acc + e):
		if k <= (acc + r):
			q += 1
		return (q/2 + q%2,q/2)
	return bathroom_partition(power+1, n-e, e*2, k, acc + e)

ina = raw_input()
for l in range(0,int(ina)):
	inb = raw_input()
	[a,b] = str(inb).split()
	if a == b:
		(max_,min_) = (0,0)
	else:
		# (max_,min_) = kth_neighbours([[0,1,int(a)]],int(b))
		(max_,min_) = bathroom_partition(1, int(a), 1, int(b), 0)
	res = str(max_) + ' ' + str(min_)
	
	case = l + 1
	name = 'Case #' + str(case) + ':'
	print name,str(res)
