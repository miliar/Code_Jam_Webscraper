import heapq
testfile = open('C-small-1-attempt0.in', 'r')
outfile = open('output.txt', 'w')

# listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
# listForTree.sort()
# listForTree.i
# listForTree.push(12)
# heapq.heapify(listForTree)             # for a min heap
# heapq._heapify_max(listForTree) 
# print listForTree

def getAnswer(stalls, shitters):
	heap = [stalls]
	# print heap
	for i in range(shitters - 1):
		space = heap.pop()
		if space == 0 or space == 1:
			heap.insert(0, 0)
		elif space % 2 == 0:
			newSpace = space / 2
			newSpace2 = newSpace - 1
			heap.append(newSpace)
			heap.append(newSpace2)
			heap.sort()
		else:
			newSpace = (space - 1) / 2
			heap.append(newSpace)
			heap.append(newSpace)
			heap.sort()
	# after
	largest = heap.pop()
	if largest == 0:
		return (0, 0)
	if largest % 2 == 0:
		ans = largest / 2
		return (ans, ans - 1)
	else:
		ans = (largest - 1) / 2
		return (ans, ans)


def main():
	test_cases = int(testfile.readline().strip())
	for i in range(test_cases):
		inputs = testfile.readline().strip().split()
		stalls = int(inputs[0])
		shitters = int(inputs[1])
		# print stalls, shitters
		(y, z) = getAnswer(stalls, shitters)
		# print answer
		outfile.write("Case #" + str(i + 1) + ": " + str(y) + " " + str(z))
		if(i + 1 < test_cases):
			outfile.write('\n')



main()

