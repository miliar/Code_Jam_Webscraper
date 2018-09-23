
def tiy(num):
	num1= list(str(num))
	num2 =  ''.join(sorted(str(num)))	
	if len(num1)==1 or num2 == str(num):
		return num
	else:
		for i in range(len(num1)):
			comps = int(num1[i])
			# print(num1)
			if i == 0 or nummax <= comps:
				nummax = comps
				pos = i
			elif nummax > comps:
				for i2 in range(i,len(num1)):
					num1[i2] = '9' 
				num1[i-1] = str(int(num1[i-1])-1)
				i = 0
				return tiy(int(''.join(num1)))
		return int(''.join(num1))

def main():
	num=int(input())
	# num = 1
	num_a = []
	for x in range(1,num+1):
		num2 = int(input())
		# print(tiy(num2))
		num_a.append(tiy(num2))

	for x in range(1,num+1):
		print("Case #"+str(x)+": "+str(num_a[x-1]))



		# print(x)
		



if __name__ == '__main__':
	main()