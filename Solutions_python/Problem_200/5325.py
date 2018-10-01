import sys, os

with open(os.getcwd() +'/numbers.txt', 'r') as f:
	content = f.read().splitlines()
	t = content[0]
	for i in range(0,int(t)):
		n = int(content[i+1])
		#Do a few easy cases without a loop for efficiency
		if n < 10:
			print('Case #' + str(i+1) + ': ' + str(n))
		elif n < 200 and (n % 10 ==0): #every number one less than a multiple of 10 up to 200 is non-decreasing
			print('Case #' + str(i+1) + ': ' + str(n-1))
		elif n < 1100 and (n%100 == 0):
			print('Case #' + str(i+1) + ': ' + str(n-1))
		elif n < 11000 and (n%1000 == 0):
			print('Case #' + str(i+1) + ': ' + str(n-1))
		else:
			nStr = str(n)
			tidy = True
			for j in range(0,len(nStr) -1):
				if int(nStr[j]) > int(nStr[j+1]):
					tidy = False
					break
			if tidy:
				print('Case #' + str(i+1) + ': ' + str(n))
			else:				
				for j in range(n-1,0,-1):
					nStr = str(j)
					tidy = True
					for k in range(0,len(nStr) -1):
						if int(nStr[k]) > int(nStr[k+1]):
							tidy = False
							break
					if tidy:
						print('Case #' + str(i+1) + ': ' + nStr)
						break