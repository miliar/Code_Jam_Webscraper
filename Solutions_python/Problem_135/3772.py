def magic(a1, a2, n1, n2):
	arr1 = a1[n1-1]
	arr2 = a2[n2-1]
	n = len(set(arr1)-set(arr2))
	if (n == 3):
		return list(set(arr1)-(set(arr1)-set(arr2)))[0]
	elif (n == 4):
		return 'Volunteer cheated!'
	else:
		return 'Bad magician!'

def main():				
	f = open('A-small-attempt0.in','r')
	n = eval(f.readline())
	output = []
	for i in range(n):
		n1 = eval(f.readline())
		v1 = list(map(eval, f.readline().split(' ')))
		v2 = list(map(eval, f.readline().split(' ')))
		v3 = list(map(eval, f.readline().split(' ')))
		v4 = list(map(eval, f.readline().split(' ')))
		a1 = [v1, v2, v3, v4]
		n2 = eval(f.readline())
		v1 = list(map(eval, f.readline().split(' ')))
		v2 = list(map(eval, f.readline().split(' ')))
		v3 = list(map(eval, f.readline().split(' ')))
		v4 = list(map(eval, f.readline().split(' ')))
		a2 = [v1, v2, v3, v4]
		output.append(magic(a1,a2,n1,n2))
	f.close()	
	ostr = ''
	for i in range(len(output)):
		ostr = ostr+ 'Case #' + str(i+1) + ': ' + str(output[i]) + '\n'
	f = open('outputf','w')
	f.write(ostr)			