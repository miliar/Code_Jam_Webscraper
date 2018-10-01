import sys

def process(s, case):
	sub = {}
	inputArray = s.split()
	index = 1
	for i in range(int(inputArray[0])):
		item = inputArray[i+1]
		sub[item[:2]] = item[2:]
		sub[item[:2][::-1]] = item[2:]
		index += 1
	
	
	temp = {}
	for j in range(int(inputArray[index])):
		item = inputArray[index+j+1]
		temp[item[0]] = item[1]
		temp[item[1]] = item[0]
	
	
	inputs = inputArray[-1]
	result = '-'
	for k in inputs:
		if result[-1]+k in sub.keys():
			result = result[:-1]+ sub[result[-1]+k]
		elif k in temp.keys() and temp[k] in result:
			result = '-'
		else:
			result += k
	
	
	result = result[1:]
	output = 'Case #' + str(case) + ': ['
	for k in result:
		output += k + ', '
	
	if len(result) > 0:
		return output[:-2] + ']'
	else:
		return output + ']'




filename = sys.argv[1]
f = open(filename, 'r')
inputs = f.readlines()
case = 1
outputs = []
for i in inputs[1:]:
	outputs.append(process(i,case)+'\n')
	case += 1


fo = open('m_out.txt','w+')
fo.writelines(outputs)
fo.close()
f.close()	