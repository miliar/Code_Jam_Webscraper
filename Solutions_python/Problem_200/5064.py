t = int(input())
for i in range(t):

	x = int(input());
	ls = []
	ls.extend(str(x));

	while (ls!=sorted(ls)):
		x-=1;
		ls = []
		ls.extend(str(x));
		

	print("Case #"+ str(i+1) + ": " +str(x))



