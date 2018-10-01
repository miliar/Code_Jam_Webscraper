
# element at index 0 is always max
def add_to_max_heap(heap, triplet):
    if len(heap) == 0:
        heap.append(triplet)
        return
    
    index = 0
    for element in heap:
        if max(element) < max(triplet):
            break;
        index += 1
    if index == len(heap):
        heap.append(triplet)
    else:
        heap.insert(index, triplet)
         
# element at index 0 is always min
def add_to_min_heap(heap, triplet):
    if len(heap) == 0:
        heap.append(triplet)
        return

    index = len(heap)
    while max(heap[index - 1]) > max(triplet) and index > 0:
        index -= 1
    if index == len(heap):
        heap.append(triplet)
    else:
        heap.insert(index, triplet)
    



T = 0
lines = []
input_file = open('Dancing_With_the_Googlers.small.input', 'r')
input_file_lines = input_file.readlines()
T = int(input_file_lines[0])
line_number = 0
for line in input_file_lines:
    if line_number > 0:
        lines.append(line.rstrip('\n').split(' '))
    line_number += 1
    if line_number > T:
        break
#===============================================================================
results = []
j = 1
for line in lines:
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    max_scores = []
    for i in range(0, N):
        max_scores.append(int(line[3 + i]))    
    results.append('Case #' + str(j) + ': ' + str(bestResult(max_scores, S, p))) 
    j += 1
        

#print bestResult([29, 20, 8, 18, 18, 21], 2, 8)

#===============================================================================

output_file = open('Dancing_With_the_Googlers.small.output', 'w')

for line in results:
    output_file.write(str(line))
    output_file.write('\n')
