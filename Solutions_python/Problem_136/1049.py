def solve(C,F,X):
	print C,F,X
	rate = (F*X)/C - F 
	print "rate = " + str(rate)
	r = 2
	ans = 0
	i = 0
	while r < rate:
		r = r + F
		ans = ans + C/(i+2)
		print C/(i+2)
		i = i + F
		# print ans
	return format(ans + X/r,'.7f')
	return 
 


g = open("B-out-large.txt","w")


f = open("B-in-large.txt","r")
d = f.read().split("\n")
n = int(d[0])

j = 1
for i in range(1,n+1):
	instance = [float(x) for x in d[i].split(" ")]
	C = instance[0]
	F = instance[1]
	X = instance[2]

	g.write ("Case #" + str(i) + ": " + solve(C,F,X) + "\n")