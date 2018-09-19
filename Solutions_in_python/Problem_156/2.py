import heapq
def check(array, specials):
	if specials >= 9:
		return specials
	array.append(int(array[0] / 2))
	array[0] = int(array[0] / 2 + array[0] % 2)
	specials = specials + 1
	array.sort(reverse=True)
	if array[0] > 2:
		return min(specials + array[0], check3(array[:], specials), check(array[:], specials))
	else:
		return min(specials + array[0], check(array[:], specials))

def check3(array, specials):
	if specials >= 9:
		return specials
	if(array[0] > 7):
		array.append(3)
		array.append(3)
		array[0] = array[0] - 6
	elif(array[0] > 4):
		array.append(2)
		array.append(2)
		array[0] = array[0] - 4
	elif(array[0] == 3 or array[0] == 4):
		array.append(1)
		array.append(1)
		array[0] = array[0] - 2
	specials = specials + 2
	array.sort(reverse=True)
	if array[0] > 2:
		return min(specials + array[0], check3(array[:], specials), check(array[:], specials))
	else:
		return min(specials + array[0], check(array[:], specials))
	
f = open('2.in')
out = open('2-out', 'w')
t = int(f.readline())
case = 1
for i in range(t):
	d = int(f.readline())
	specials = 0
	heap = [int(x) for x in f.readline().strip().split()]
	heap.sort(reverse=True)
	minim = heap[0]
	print('********')
	print(case)
	print(heap)
	if heap[0] > 2:
		minim = min(minim, check3(heap[:], 0), check(heap[:], 0))
	else:
		minim = min(minim, check(heap[:], 0))
	print(minim)
	print('*****')
	out.write('Case #' + str(case) + ': ' + str(minim) + '\n')
	case = case + 1
out.close()
