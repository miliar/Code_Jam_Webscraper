# main.py
from heapq import heappush
from heapq import heappop

def get_stalls_condition(stall_num, person_num):
	heap = [stall_num]
	person_it = 1

	while(person_it < person_num):
		split_result = get_split_result(heap.pop())
		for key in split_result:
			heap.append(key)
		heap = sorted(heap)
		person_it+=1

	x = heap.pop()
	# print(x)
	return get_split_result(x)


def get_split_result(stall_num):
	min_stall = (stall_num-1) // 2
	max_stall = min_stall + ((stall_num-1) % 2)

	return [min_stall, max_stall]


######### MAIN #########
import inputhandler as ih
import sys

if __name__ == "__main__":
	filename = sys.argv[1]
	inputs = ih.get_input(filename)
	num = int(inputs[0])

	for i in range(1,num+1):
		num_stalls = int(inputs[i].split()[0])
		num_person = int(inputs[i].split()[1])
		result = get_stalls_condition(num_stalls,num_person)		
		print("Case #{:d}: {:d} {:d}".format(i,result.pop(), result.pop()))