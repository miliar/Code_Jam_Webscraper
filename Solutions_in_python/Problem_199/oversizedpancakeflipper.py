def frkn(s,k,c):
	while s != [] and s[0] == "+":
		del s[0]
 	if s == []:
		return c
	if len(s) < k:
		return "IMPOSSIBLE"
	for i in range(k):
		if s[i] == "-":
			s[i] = "+"
		else:
			s[i] = "-"
	c += 1
	return frkn(s,k,c)

inp = open("/root/Desktop/input.txt","r")
output = open("/root/Desktop/output.txt","w")

inp_ = inp.read().splitlines()

i = 1

for x in inp_:
	m = x.split(" ")
	s = list(m[0])
	out = "Case #{}: {}\n".format(i,frkn(s,int(m[1]),0))
	output.write(out)
	i += 1

inp.close()	
output.close()

x = 0

"""while x != "x":
	s = input("list: ")
	k = input("number: ")

	s = list(s)
	print s
	print frkn(s,k,0)"""








