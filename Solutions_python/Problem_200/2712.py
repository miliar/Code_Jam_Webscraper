test=int(input())
for x in range(test):
	original=input()
	string = original
	number= int(string)
	l=len(string)
	flag=0
	for y in range(l-1,0,-1):
		if(int(string[y])<int(string[y-1])):
			number=number-(1*(10**(l-y)))
			flag=y
			string=str(number)
	if flag>0:
		number=number-number%(10**(l-flag))
		number=number+((10**(l-flag))-1)
	print ("Case #" + str(x+1) + ": " + str(number))