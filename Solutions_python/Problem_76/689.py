import sys

def xor(a,b):
	return a^b


def candy(s,case_num):
	l = [int(i) for i in s.split()]
	output = str(sum(l)-min(l)) if reduce(xor, l) == 0 else 'NO'	
	return 'Case #' + str(case_num) + ': ' + output


filename = sys.argv[1]
f = open(filename, 'r')
inputs = f.readlines()
case_num = 1
outputs = []
for i in range(2,len(inputs),2):
	outputs.append(candy(inputs[i],case_num)+'\n')
	case_num += 1


fo = open(filename.split('.')[0]+'.out','w+')
fo.writelines(outputs)
fo.close()
f.close()	