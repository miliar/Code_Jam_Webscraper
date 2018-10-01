import bisect

def frkn(n,k):
	n = int(n); k = int(k); A = [n]; i = 1
	while k > i:
		x = (A[-1]-1)/2
		bisect.insort(A,A[-1]-1-x)
		bisect.insort(A,x)
		del A[-1]
		i += 1
	x = (A[-1]-1)/2
	return "{} {}".format(A[-1]-1-x, x)



inp = open("/root/Desktop/input.txt","r")
output = open("/root/Desktop/output.txt","w")

inp_ = inp.read().splitlines()

i = 1

for x in inp_:
	x = x.split(" ")
	out = "Case #{}: {}\n".format(i,frkn(x[0],x[1]))
	output.write(out)
	i += 1

inp.close()	
output.close()









