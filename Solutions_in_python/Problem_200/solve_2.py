import csv

count = 1
length = 0
data = []

#with open('test_2.txt', 'rb') as csvfile:
with open('2_in.txt', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter= ' ')
	for row in reader:
	    if count == 1:
	    	length = row[0]
	    else:
	    	data.append(row)
	    count += 1

def check_clean(array, index):
	print "checking", array, index
	for i in range(1, index+1):
		if int(array[i]) < int(array[i-1]):
			return 0
	return 1

def decrement(array, index): 
	print "decrement: ", array, index
	val = array[index]
	i = index
	if i != 0:
		while i >= 0:
			if array[i - 1] == array[index]:
				i -= 1
			else:
				break
	print "decrementing index: ", i
	array[i] = str(int(array[i]) - 1)
	for j in range(i + 1, len(array)):
		array[j] = '9'
	return array

case_num = 0
status = ''
for row in data:
	case_num += 1
	row = row[0]
	array = list(row)
	for i in range(1, len(array)):
		if check_clean(array, i) == 0:
			if array[i] >= 1:
				array = decrement(array, i-1)
	answer = "".join(array)
	if answer[0] == "0":
		answer = answer[1:len(answer)]

	status += 'Case #' + str(case_num) + ': ' + str(answer) + '\n'
			
print status
with open('2_out.txt', 'w') as out:
	out.write(status)